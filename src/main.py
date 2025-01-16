from otp_verification import OTPVerification
from email_service import EmailService
import config

def main():
    # receiver_email = config.RECEIVER_EMAIL
    receiver_email = input("Enter your email address: ")
    while not receiver_email.endswith("iitrpr.ac.in"):
        print("Please enter your IIT Ropar email address which ends with 'iitrpr.ac.in'")
        receiver_email = input("Enter your email address: ")
    print("Your email address is:", receiver_email)

    otp_verification = OTPVerification()
    otp = otp_verification.generate_otp()

    # Gmail SMTP settings
    smtp_server = config.SMTP_SERVER
    port = config.PORT
    username = config.USERNAME
    password = config.PASSWORD

    email_service = EmailService(smtp_server, port, username, password)
    otp_verification.send_otp(receiver_email, email_service)

    user_otp = input("Enter the OTP sent to your email: ")
    if otp_verification.verify_otp(user_otp):
        print("OTP verified successfully!")
    else:
        print("Invalid OTP. Please try again.")

if __name__ == "__main__":
    main()