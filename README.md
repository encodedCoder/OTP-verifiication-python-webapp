# IIT Connect

IIT Connect is a web application that allows users to log in using their IIT Ropar email address and receive a One-Time Password (OTP) for verification. The application also supports test emails for development purposes.

## Features

- User login with IIT Ropar email address or test emails
- OTP verification for secure login
- User registration with additional details
- Dashboard displaying user details
- Common header and footer across all pages

## Prerequisites

- Python 3.x
- MongoDB (local or MongoDB Atlas)
- Flask
- Required Python packages (listed in `requirements.txt`)

## Project Structure

```
iit-connect/
├── src/
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── verify.html
│   │   └── dashboard.html
│   ├── static/
│   │   ├── styles.css
│   │   └── images/
│   ├── app.py
│   ├── config.py
│   ├── email_service.py
│   ├── main.py
│   ├── otp_verification.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
```

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/encodedcoder/iitconnect22.git
   cd iitconnect22
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Set up MongoDB:

- If using MongoDB Atlas, create a cluster and get the connection string.
- If using local MongoDB, ensure the MongoDB server is running.

4. Update the config.py file with your MongoDB connection string and email service credentials:

```
SMTP_SERVER = "smtp.gmail.com"
PORT = 587
USERNAME = "your_email@gmail.com"
PASSWORD = "your_email_password"
RECEIVER_EMAIL = "receiver_email@gmail.com"
MONGO_URI = "your_mongodb_connection_string"
TEST_EMAILS = ["test1@example.com", "test2@example.com"]
```

## Usage

1. Run the application:

   ```
   python app.py
   ```

2. Open your web browser and navigate to http://127.0.0.1:5000/ to access the login interface.

## Dependencies

- `smtplib` for handling email sending.
- Any additional libraries required for OTP generation and verification will be listed in `requirements.txt`.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

# Usage

## Login

Enter your IIT Ropar email address or a test email from the TEST_EMAILS list.
Click "Send OTP" to receive an OTP via email.
Enter the OTP on the verification page to log in.

## Registration

1. If logging in for the first time, you will be redirected to the registration page.

2. Fill in your details (name, phone number, course, department, enrollment date, and optional completion date).

3. Submit the form to complete your registration.

## Dashboard

1. After logging in, you will be redirected to the dashboard.

2. The dashboard displays your registered details.

## Logout

1. Click the "Logout" link in the header to log out.

## License

This project is licensed under the MIT License.
