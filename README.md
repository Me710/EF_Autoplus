# EF AUTO+ - Application Web Dynamique

Application web moderne pour la gestion d'un concessionnaire automobile avec back office complet.

## 🚀 Fonctionnalités

### Site Public
- **Page d'accueil** avec section héro et présentation
- **Catalogue de véhicules** dynamique avec filtres
- **Formulaire d'échange** de véhicules avec upload de photos
- **Formulaire de contact** pour les clients
- **Design responsive** et moderne

### Back Office
- **Authentification sécurisée** pour les administrateurs
- **Tableau de bord** avec statistiques
- **Gestion des véhicules** (ajout, modification, suppression) avec **upload d'images**
- **Gestion des demandes d'échange** avec statuts et **système de réponses**
- **Gestion des messages de contact** avec statuts et **système de réponses**
- **Interface d'administration** moderne et intuitive

## 🆕 Nouvelles Fonctionnalités

### Upload d'Images
- **Upload direct** d'images pour les véhicules
- **Prévisualisation** des images actuelles lors de l'édition
- **Gestion automatique** des fichiers avec noms sécurisés
- **Support** des formats JPG, PNG, JPEG, GIF, WEBP
- **Validation** des types de fichiers
- **Affichage correct** sur le site public et dans le back office

### Système de Réponses
- **Réponses aux demandes d'échange** avec historique
- **Réponses aux messages de contact** avec historique
- **Statuts automatiques** mis à jour lors des réponses
- **Interface dédiée** pour chaque type de réponse

### Optimisation SEO 🚀
- **Balises meta complètes** avec mots-clés ciblés pour Québec
- **Données structurées Schema.org** pour AutoDealer
- **Open Graph et Twitter Cards** pour partage sur réseaux sociaux
- **Géolocalisation précise** pour recherches locales
- **Fichiers robots.txt et sitemap.xml** pour meilleure indexation
- **Mots-clés optimisés** pour la région de Québec et environs
- **Guide SEO complet** (voir SEO_GUIDE.md)

## 🛠️ Technologies Utilisées

- **Backend**: Flask (Python)
- **Base de données**: SQLite avec SQLAlchemy
- **Frontend**: HTML5, CSS3, JavaScript
- **Framework CSS**: Tailwind CSS
- **Icônes**: Font Awesome
- **Authentification**: Flask-Login

## 📋 Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

## 🔧 Installation

1. **Cloner le projet**
   ```bash
   git clone <url-du-repo>
   cd EF_Autoplus
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement virtuel**
   
   **Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

5. **Lancer l'application**
   ```bash
   python app.py
   ```

6. **Accéder à l'application**
   - Site public: http://localhost:5000
   - Back office: http://localhost:5000/admin/login

## 🔐 Accès Back Office

**Identifiants par défaut:**
- **Nom d'utilisateur**: `admin`
- **Mot de passe**: `admin123`

⚠️ **Important**: Changez ces identifiants après la première connexion !

## 📁 Structure du Projet

```
EF_Autoplus/
├── app.py                 # Application Flask principale
├── requirements.txt       # Dépendances Python
├── email_config.py        # Configuration emails (futur)
├── add_sample_data.py     # Script données d'exemple
├── README.md             # Documentation
├── static/               # Fichiers statiques
│   ├── css/
│   │   └── styles.css    # Styles personnalisés
│   ├── js/
│   │   └── script.js     # JavaScript frontend
│   ├── images/           # Images du site
│   └── uploads/          # Photos uploadées (créé automatiquement)
├── templates/            # Templates HTML
│   ├── index.html        # Page d'accueil
│   └── admin/            # Templates du back office
│       ├── base.html     # Template de base admin
│       ├── login.html    # Page de connexion
│       ├── dashboard.html # Tableau de bord
│       ├── vehicles.html # Gestion des véhicules
│       ├── add_vehicle.html # Ajout de véhicule
│       ├── edit_vehicle.html # Édition de véhicule
│       ├── exchanges.html # Gestion des échanges
│       ├── respond_exchange.html # Répondre aux échanges
│       ├── contacts.html # Gestion des contacts
│       └── respond_contact.html # Répondre aux contacts
└── ef_autoplus.db        # Base de données SQLite (créée automatiquement)
```

## 🗄️ Base de Données

L'application utilise SQLite avec les tables suivantes :

- **User**: Utilisateurs administrateurs
- **Vehicle**: Véhicules du catalogue
- **ExchangeRequest**: Demandes d'échange de véhicules
- **ExchangeResponse**: Réponses aux demandes d'échange
- **ContactMessage**: Messages de contact
- **ContactResponse**: Réponses aux messages de contact

## 🔧 Configuration

### Variables d'environnement (optionnel)

Créez un fichier `.env` à la racine du projet :

```env
FLASK_SECRET_KEY=votre_clé_secrète_très_longue
DATABASE_URL=sqlite:///ef_autoplus.db
UPLOAD_FOLDER=static/uploads
```

### Personnalisation

1. **Logo**: Remplacez `static/images/ef_autoplus_logo.jpg`
2. **Images héro**: Remplacez les images dans `static/images/`
3. **Couleurs**: Modifiez les classes Tailwind dans les templates
4. **Styles**: Éditez `static/css/styles.css`

## 📱 Utilisation

### Ajouter un véhicule

1. Connectez-vous au back office
2. Allez dans "Véhicules" → "Ajouter un véhicule"
3. Remplissez le formulaire avec :
   - Nom du véhicule
   - Type (Berline, SUV, Camion, Luxe)
   - Prix
   - **Image du véhicule** (upload direct)
   - Informations techniques (optionnel)

### Répondre aux demandes d'échange

1. Dans le back office, allez dans "Demandes d'échange"
2. Cliquez sur l'icône **réponse** (🔄) à côté de la demande
3. Consultez les détails de la demande
4. Tapez votre réponse dans le formulaire
5. Envoyez la réponse (le statut sera automatiquement mis à jour)

### Répondre aux messages

1. Dans "Messages", cliquez sur l'icône **réponse** (🔄)
2. Consultez le message complet
3. Tapez votre réponse
4. Envoyez la réponse (le statut sera automatiquement mis à jour)

### Gérer les statuts

- **Demandes d'échange**: En attente → En cours → Terminé/Annulé
- **Messages**: Non lu → En cours → Répondu

## 🚀 Déploiement

### Production

Pour déployer en production :

1. **Sécuriser l'application**
   ```python
   # Dans app.py
   app.secret_key = os.environ.get('SECRET_KEY', 'clé_très_longue_et_complexe')
   ```

2. **Utiliser un serveur WSGI**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

3. **Configurer un reverse proxy** (Nginx/Apache)

4. **Sauvegarder la base de données** régulièrement

### Docker (optionnel)

Créez un `Dockerfile` :

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🐛 Dépannage

### Problèmes courants

1. **Erreur de base de données**
   - Supprimez `ef_autoplus.db` et relancez l'application
   - La base sera recréée automatiquement

2. **Erreur d'upload**
   - Vérifiez que le dossier `static/uploads` existe
   - Vérifiez les permissions d'écriture

3. **Problème de connexion admin**
   - Vérifiez que l'utilisateur admin a été créé
   - Consultez les logs de l'application

## 🔍 Optimisation SEO

Consultez le fichier **SEO_GUIDE.md** pour :
- Les optimisations déjà implémentées
- Les prochaines étapes pour améliorer le référencement
- Les outils et métriques à suivre
- Un plan d'action détaillé

### Informations de Contact
- **Adresse** : 11 Av Ste-Brigitte, Ste-Brigitte-de-Laval, QC G0A 3K0, Canada
- **Téléphone** : (514) 718-8041
- **Email** : efautoplus1@gmail.com
- **Heures** : Lun-Ven 9h-18h | Sam 9h-17h | Dim sur rendez-vous

## 📞 Support

Pour toute question ou problème :
- Vérifiez les logs de l'application
- Consultez la documentation Flask
- Consultez le guide SEO (SEO_GUIDE.md)
- Ouvrez une issue sur le repository

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

---

**EF AUTO+** - Votre expert automobile à Québec 🚗 