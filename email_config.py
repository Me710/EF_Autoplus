# Configuration pour l'envoi d'emails
# À implémenter dans le futur pour envoyer automatiquement les réponses par email

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os

class EmailSender:
    def __init__(self):
        # Configuration SMTP (à configurer selon votre fournisseur)
        self.smtp_server = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = int(os.environ.get('SMTP_PORT', 587))
        self.email = os.environ.get('EMAIL_ADDRESS', '')
        self.password = os.environ.get('EMAIL_PASSWORD', '')
        
    def send_exchange_response(self, exchange_request, admin_message):
        """Envoie une réponse par email pour une demande d'échange"""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = exchange_request.email
            msg['Subject'] = f"Réponse à votre demande d'échange - EF AUTO+"
            
            body = f"""
            Bonjour {exchange_request.name},
            
            Nous avons bien reçu votre demande d'échange pour votre véhicule : {exchange_request.vehicle}
            
            Voici notre réponse :
            
            {admin_message}
            
            Nous vous contacterons bientôt pour la suite.
            
            Cordialement,
            L'équipe EF AUTO+
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Envoi de l'email (désactivé pour le moment)
            # self._send_email(msg)
            
            return True
        except Exception as e:
            print(f"Erreur lors de l'envoi de l'email : {e}")
            return False
    
    def send_contact_response(self, contact_message, admin_message):
        """Envoie une réponse par email pour un message de contact"""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = contact_message.email
            msg['Subject'] = f"Réponse à votre message - EF AUTO+"
            
            body = f"""
            Bonjour {contact_message.name},
            
            Nous avons bien reçu votre message concernant : {contact_message.subject}
            
            Voici notre réponse :
            
            {admin_message}
            
            N'hésitez pas à nous recontacter si vous avez d'autres questions.
            
            Cordialement,
            L'équipe EF AUTO+
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Envoi de l'email (désactivé pour le moment)
            # self._send_email(msg)
            
            return True
        except Exception as e:
            print(f"Erreur lors de l'envoi de l'email : {e}")
            return False
    
    def _send_email(self, msg):
        """Méthode privée pour envoyer l'email via SMTP"""
        if not all([self.email, self.password]):
            print("Configuration email incomplète")
            return False
            
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email, self.password)
            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            print(f"Erreur SMTP : {e}")
            return False

# Instance globale
email_sender = EmailSender() 