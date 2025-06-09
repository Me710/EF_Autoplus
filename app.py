from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # pour les messages flash

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_exchange', methods=['POST'])
def submit_exchange():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    vehicle = request.form.get('vehicle')
    message = request.form.get('message')
    #fichier photo = request.files['photo']
    flash("Votre demande d'échange a été reçue. Merci !")
    return redirect(url_for('home'))

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form.get('contact-name')
    email = request.form.get('contact-email')
    subject = request.form.get('contact-subject')
    message = request.form.get('contact-message')
    flash("Votre message a été envoyé. Merci !")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
