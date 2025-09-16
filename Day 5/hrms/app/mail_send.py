import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import app_password, from_address, to_address  # Make sure config.py is in the same folder

def send_gmail(to_address, subject, body):
    """
    Send an email via Gmail SMTP using app password authentication.
    
    Args:
        to_address (str): Recipient email address
        subject (str): Email subject line
        body (str): Plain text email body
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = from_address
        msg["To"] = to_address
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to Gmail SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Secure connection
        server.login(from_address, app_password)  # Login using app password
        server.send_message(msg)
        server.quit()

        print(f"Email sent successfully to {to_address}")
        return True
    except Exception as e:
        print("Error sending email:", e)
        return False

# Test the function by sending a mail to the default `to_address` from config.py
if __name__ == "__main__":
    subject = "Maheswaran - Test Subject from pystud19 - 16-09-2025"
    body = "Hello from Python!"
    result = send_gmail(to_address, subject, body)
    print("Mail sent successfully?", result)

