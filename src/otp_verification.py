import random
import string
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

OTP_TIMEOUT = 600  # 600 seconds = 10 minutes

class OTPVerification:
    def __init__(self):
        self.generated_otp = None
        self.otp_generation_time = None

    def generate_otp(self, length=6):
        """Generate a random OTP of specified length."""
        self.generated_otp = ''.join(random.choices(string.digits, k=length))
        self.otp_generation_time = time.time()
        return self.generated_otp

    def send_otp(self, email, email_service):
        """Send the generated OTP to the specified email address."""
        if self.generated_otp is None:
            raise ValueError("OTP has not been generated.")

        email_subject = "IIT Connect OTP Verification"
        email_message = f"""
        <!DOCTYPE html>
        <html>
            <body>
            <h1>Welcome to IIT Connect</h1>
            <p>Your Login OTP code is: <b>{self.generated_otp}</b></p>
            <p>This OTP is valid for 10 minutes. Please do not share this OTP with anyone.</p>
            <p>If you did not request this OTP, please ignore this email.</p>
            <p>This email was sent from the domain <a href="https://iitconnect.vercel.app/">iitconnect.vercel.app</a> for the purpose of verifying your login attempt.</p>
            <p><a href="https://iitconnect.vercel.app/">Visit IIT Connect</a></p>
            </body>
        </html>
        """

        email_service.send_email(email, email_subject, email_message)

    def verify_otp(self, user_otp):
        """Verify the provided OTP against the generated OTP."""
        if self.generated_otp is None:
            return False

        current_time = time.time()
        if current_time - self.otp_generation_time > OTP_TIMEOUT:
            return False

        return user_otp == self.generated_otp

