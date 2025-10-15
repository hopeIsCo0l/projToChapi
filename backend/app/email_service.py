import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def send_confirmation_email(email: str) -> bool:
    """
    Send confirmation email to the user.
    For now, this is a stub function that prints to console.
    In production, this would send actual emails.
    """
    try:
        print(f"📧 Confirmation email would be sent to: {email}")
        print(f"📧 Email content: 'Thank you for joining our waitlist! We'll notify you when we launch.'")
        
        # TODO: Implement actual email sending
        # smtp_host = os.getenv("SMTP_HOST")
        # smtp_port = int(os.getenv("SMTP_PORT", 587))
        # smtp_username = os.getenv("SMTP_USERNAME")
        # smtp_password = os.getenv("SMTP_PASSWORD")
        
        # if all([smtp_host, smtp_username, smtp_password]):
        #     msg = MIMEMultipart()
        #     msg['From'] = smtp_username
        #     msg['To'] = email
        #     msg['Subject'] = "Welcome to our waitlist!"
        #     
        #     body = "Thank you for joining our waitlist! We'll notify you when we launch."
        #     msg.attach(MIMEText(body, 'plain'))
        #     
        #     server = smtplib.SMTP(smtp_host, smtp_port)
        #     server.starttls()
        #     server.login(smtp_username, smtp_password)
        #     text = msg.as_string()
        #     server.sendmail(smtp_username, email, text)
        #     server.quit()
        
        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False

