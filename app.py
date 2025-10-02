from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from email_config import email_sender

app = Flask(__name__)
app.secret_key = 'supersecretkey123456789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ef_autoplus.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Créer le dossier uploads s'il n'existe pas
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Fonction pour valider les types de fichiers
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin_login'

# Modèles de base de données
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text)
    year = db.Column(db.Integer)
    mileage = db.Column(db.String(50))
    fuel_type = db.Column(db.String(50))
    transmission = db.Column(db.String(50))
    is_available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ExchangeRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    vehicle = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text)
    photo_path = db.Column(db.String(500))
    status = db.Column(db.String(20), default='En attente')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Non lu')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ExchangeResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exchange_request_id = db.Column(db.Integer, db.ForeignKey('exchange_request.id'), nullable=False)
    admin_message = db.Column(db.Text, nullable=False)
    response_date = db.Column(db.DateTime, default=datetime.utcnow)
    exchange_request = db.relationship('ExchangeRequest', backref=db.backref('responses', lazy=True))

class ContactResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_message_id = db.Column(db.Integer, db.ForeignKey('contact_message.id'), nullable=False)
    admin_message = db.Column(db.Text, nullable=False)
    response_date = db.Column(db.DateTime, default=datetime.utcnow)
    contact_message = db.relationship('ContactMessage', backref=db.backref('responses', lazy=True))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes SEO
@app.route('/robots.txt')
def robots():
    return send_from_directory(app.root_path, 'robots.txt')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(app.root_path, 'sitemap.xml')

# Routes publiques
@app.route('/')
def home():
    vehicles = Vehicle.query.filter_by(is_available=True).all()
    return render_template('index.html', vehicles=vehicles)

@app.route('/test-images')
def test_images():
    """Route de test pour vérifier l'affichage des images"""
    vehicles = Vehicle.query.all()
    return render_template('test_images.html', vehicles=vehicles)

@app.route('/vehicule/<int:id>')
def vehicle_details(id):
    """Page de détails d'un véhicule"""
    vehicle = Vehicle.query.get_or_404(id)
    # Récupérer d'autres véhicules similaires pour les suggestions
    similar_vehicles = Vehicle.query.filter(
        Vehicle.type == vehicle.type,
        Vehicle.id != vehicle.id,
        Vehicle.is_available == True
    ).limit(3).all()
    return render_template('vehicle_details.html', vehicle=vehicle, similar_vehicles=similar_vehicles)

@app.route('/api/vehicles')
def api_vehicles():
    vehicles = Vehicle.query.filter_by(is_available=True).all()
    return jsonify([{
        'id': v.id,
        'name': v.name,
        'type': v.type,
        'price': v.price,
        'image': v.image_url if v.image_url.startswith('http') else url_for('static', filename=v.image_url),
        'description': v.description,
        'year': v.year,
        'mileage': v.mileage,
        'fuel_type': v.fuel_type,
        'transmission': v.transmission
    } for v in vehicles])

@app.route('/submit_exchange', methods=['POST'])
def submit_exchange():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    vehicle = request.form.get('vehicle')
    message = request.form.get('message')
    
    photo_path = None
    if 'photo' in request.files:
        file = request.files['photo']
        if file and file.filename:
            filename = secure_filename(file.filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{timestamp}_{filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            photo_path = f"uploads/{filename}"
    
    exchange_request = ExchangeRequest(
        name=name,
        email=email,
        phone=phone,
        vehicle=vehicle,
        message=message,
        photo_path=photo_path
    )
    
    db.session.add(exchange_request)
    db.session.commit()
    
    flash("Votre demande d'échange a été reçue. Merci !")
    return redirect(url_for('home'))

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form.get('contact-name')
    email = request.form.get('contact-email')
    subject = request.form.get('contact-subject')
    message = request.form.get('contact-message')
    
    contact_message = ContactMessage(
        name=name,
        email=email,
        subject=subject,
        message=message
    )
    
    db.session.add(contact_message)
    db.session.commit()
    
    flash("Votre message a été envoyé. Merci !")
    return redirect(url_for('home'))

# Routes d'authentification
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Nom d\'utilisateur ou mot de passe incorrect')
    
    return render_template('admin/login.html')

@app.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()
    return redirect(url_for('admin_login'))

# Routes du back office
@app.route('/admin')
@login_required
def admin_dashboard():
    stats = {
        'vehicles': Vehicle.query.count(),
        'exchange_requests': ExchangeRequest.query.count(),
        'contact_messages': ContactMessage.query.count(),
        'pending_exchanges': ExchangeRequest.query.filter_by(status='En attente').count(),
        'unread_messages': ContactMessage.query.filter_by(status='Non lu').count()
    }
    return render_template('admin/dashboard.html', stats=stats)

@app.route('/admin/vehicles')
@login_required
def admin_vehicles():
    vehicles = Vehicle.query.order_by(Vehicle.created_at.desc()).all()
    return render_template('admin/vehicles.html', vehicles=vehicles)

@app.route('/admin/vehicles/add', methods=['GET', 'POST'])
@login_required
def admin_add_vehicle():
    if request.method == 'POST':
        name = request.form.get('name')
        type_vehicle = request.form.get('type')
        price = request.form.get('price')
        description = request.form.get('description')
        year = request.form.get('year')
        mileage = request.form.get('mileage')
        fuel_type = request.form.get('fuel_type')
        transmission = request.form.get('transmission')
        
        # Gestion de l'upload d'image
        image_path = None
        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f"vehicle_{timestamp}_{filename}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_path = f"uploads/{filename}"
            elif file and file.filename:
                flash('Type de fichier non autorisé. Utilisez PNG, JPG, JPEG, GIF ou WEBP.')
                return redirect(url_for('admin_add_vehicle'))
        
        vehicle = Vehicle(
            name=name,
            type=type_vehicle,
            price=price,
            image_url=image_path,
            description=description,
            year=year,
            mileage=mileage,
            fuel_type=fuel_type,
            transmission=transmission
        )
        
        db.session.add(vehicle)
        db.session.commit()
        flash('Véhicule ajouté avec succès')
        return redirect(url_for('admin_vehicles'))
    
    return render_template('admin/add_vehicle.html')

@app.route('/admin/vehicles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def admin_edit_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    
    if request.method == 'POST':
        vehicle.name = request.form.get('name')
        vehicle.type = request.form.get('type')
        vehicle.price = request.form.get('price')
        vehicle.description = request.form.get('description')
        vehicle.year = request.form.get('year')
        vehicle.mileage = request.form.get('mileage')
        vehicle.fuel_type = request.form.get('fuel_type')
        vehicle.transmission = request.form.get('transmission')
        vehicle.is_available = 'is_available' in request.form
        
        # Gestion de l'upload d'image
        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f"vehicle_{timestamp}_{filename}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                vehicle.image_url = f"uploads/{filename}"
            elif file and file.filename:
                flash('Type de fichier non autorisé. Utilisez PNG, JPG, JPEG, GIF ou WEBP.')
                return redirect(url_for('admin_edit_vehicle', id=vehicle.id))
        
        db.session.commit()
        flash('Véhicule modifié avec succès')
        return redirect(url_for('admin_vehicles'))
    
    return render_template('admin/edit_vehicle.html', vehicle=vehicle)

@app.route('/admin/vehicles/delete/<int:id>')
@login_required
def admin_delete_vehicle(id):
    vehicle = Vehicle.query.get_or_404(id)
    db.session.delete(vehicle)
    db.session.commit()
    flash('Véhicule supprimé avec succès')
    return redirect(url_for('admin_vehicles'))

@app.route('/admin/exchanges')
@login_required
def admin_exchanges():
    exchanges = ExchangeRequest.query.order_by(ExchangeRequest.created_at.desc()).all()
    return render_template('admin/exchanges.html', exchanges=exchanges)

@app.route('/admin/exchanges/<int:id>/status', methods=['POST'])
@login_required
def admin_update_exchange_status(id):
    exchange = ExchangeRequest.query.get_or_404(id)
    status = request.form.get('status')
    exchange.status = status
    db.session.commit()
    flash('Statut mis à jour')
    return redirect(url_for('admin_exchanges'))

@app.route('/admin/contacts')
@login_required
def admin_contacts():
    contacts = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()
    return render_template('admin/contacts.html', contacts=contacts)

@app.route('/admin/contacts/<int:id>/status', methods=['POST'])
@login_required
def admin_update_contact_status(id):
    contact = ContactMessage.query.get_or_404(id)
    status = request.form.get('status')
    contact.status = status
    db.session.commit()
    flash('Statut mis à jour')
    return redirect(url_for('admin_contacts'))

@app.route('/admin/exchanges/<int:id>/respond', methods=['GET', 'POST'])
@login_required
def admin_respond_exchange(id):
    exchange = ExchangeRequest.query.get_or_404(id)
    
    if request.method == 'POST':
        admin_message = request.form.get('admin_message')
        
        response = ExchangeResponse(
            exchange_request_id=exchange.id,
            admin_message=admin_message
        )
        
        exchange.status = 'Répondu'
        db.session.add(response)
        db.session.commit()
        
        # Envoyer l'email
        try:
            email_sender.send_exchange_response(exchange, admin_message)
            flash('Réponse envoyée avec succès et email transmis au client')
        except Exception as e:
            flash(f'Réponse enregistrée mais erreur lors de l\'envoi de l\'email: {str(e)}')
        
        return redirect(url_for('admin_exchanges'))
    
    return render_template('admin/respond_exchange.html', exchange=exchange)

@app.route('/admin/contacts/<int:id>/respond', methods=['GET', 'POST'])
@login_required
def admin_respond_contact(id):
    contact = ContactMessage.query.get_or_404(id)
    
    if request.method == 'POST':
        admin_message = request.form.get('admin_message')
        
        response = ContactResponse(
            contact_message_id=contact.id,
            admin_message=admin_message
        )
        
        contact.status = 'Répondu'
        db.session.add(response)
        db.session.commit()
        
        # Envoyer l'email
        try:
            email_sender.send_contact_response(contact, admin_message)
            flash('Réponse envoyée avec succès et email transmis au client')
        except Exception as e:
            flash(f'Réponse enregistrée mais erreur lors de l\'envoi de l\'email: {str(e)}')
        
        return redirect(url_for('admin_contacts'))
    
    return render_template('admin/respond_contact.html', contact=contact)

# Initialisation de la base de données
def init_db():
    with app.app_context():
        db.create_all()
        
        # Créer un utilisateur admin par défaut s'il n'existe pas
        if not User.query.filter_by(username='admin').first():
            admin_user = User(
                username='admin',
                password_hash=generate_password_hash('admin123'),
                email='admin@efautoplus.com'
            )
            db.session.add(admin_user)
            db.session.commit()
            print("Utilisateur admin créé: username=admin, password=admin123")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
