import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import socket

class EmailService:
    def __init__(self, smtp_server, port, username, password):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password.strip()  # Remove any whitespace from password

    def send_email(self, to_email, subject, body, image_path=None):
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))  # Specify MIME type as 'html'

        if image_path:
            with open(image_path, 'rb') as img:
                mime_image = MIMEImage(img.read())
                mime_image.add_header('Content-ID', '<image1>')
                msg.attach(mime_image)

        try:
            print(f"Resolving SMTP server address: {self.smtp_server}")
            smtp_ip = socket.gethostbyname(self.smtp_server)
            print(f"SMTP server IP address: {smtp_ip}")

            server = smtplib.SMTP(self.smtp_server, self.port)
            server.starttls()
            print("Attempting login...")
            server.login(self.username, self.password)
            print("Login successful")

            text = msg.as_string()
            server.sendmail(self.username, to_email, text)
            server.quit()
            print("Email sent successfully!")
        except smtplib.SMTPAuthenticationError as e:
            print(f"Authentication failed: {e}")
        except Exception as e:
            print(f"Failed to send email: {e}")