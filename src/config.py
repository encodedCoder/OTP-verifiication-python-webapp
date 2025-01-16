from dotenv import load_dotenv
import os

# Load environment variables from .env.local file
load_dotenv(dotenv_path='.env.local')

# Description: Configuration file for the application
SMTP_SERVER = os.getenv("SMTP_SERVER")
PORT = int(os.getenv("PORT"))
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

# Database configuration
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
USERS_COLLECTION = os.getenv("USERS_COLLECTION")

# List of test email addresses
TEST_EMAILS = os.getenv("TEST_EMAILS").split(',')