from flask import Flask, render_template, request, redirect, url_for, flash, session
from otp_verification import OTPVerification
from email_service import EmailService
from pymongo import MongoClient, errors
import config

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# MongoDB setup with error handling
try:
    client = MongoClient(config.MONGO_URI)
    db = client[config.DATABASE_NAME]
    users_collection = db[config.USERS_COLLECTION]
except errors.ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")
    # Handle the error appropriately in your application

otp_verification = OTPVerification()

@app.route('/', methods=['GET', 'POST'])
def login():
    if 'email' in session:
        user = users_collection.find_one({"email": session['email']})
        if user and user.get('details_filled'):
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('register'))

    if request.method == 'POST':
        email = request.form['email']

        if not email.endswith("iitrpr.ac.in") and email not in config.TEST_EMAILS:
            flash("Please enter your IIT Ropar email address.")
            return redirect(url_for('login'))

        otp = otp_verification.generate_otp()
        email_service = EmailService(config.SMTP_SERVER, config.PORT, config.USERNAME, config.PASSWORD)
        otp_verification.send_otp(email, email_service)
        session['email'] = email
        session['otp_generated'] = True
        return redirect(url_for('verify_otp'))

    return render_template('login.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify_otp():
    if 'email' not in session:
        return redirect(url_for('login'))

    if 'otp_generated' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        user_otp = request.form['otp']
        if otp_verification.verify_otp(user_otp):
            session.pop('otp_generated', None)
            session['logged_in'] = True
            user = users_collection.find_one({"email": session['email']})
            if user and user.get('details_filled'):
                return redirect(url_for('dashboard'))
            else:
                return redirect(url_for('register'))
        else:
            flash("Invalid OTP. Please try again.")
            return redirect(url_for('verify_otp'))

    return render_template('verify.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'email' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        course = request.form['course']
        department = request.form['department']
        enrollment_date = request.form['enrollment_date']
        completion_date = request.form.get('completion_date')

        users_collection.update_one(
            {"email": session['email']},
            {"$set": {
                "name": name,
                "phone": phone,
                "course": course,
                "department": department,
                "enrollment_date": enrollment_date,
                "completion_date": completion_date,
                "details_filled": True
            }},
            upsert=True
        )
        return redirect(url_for('dashboard'))

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    user = users_collection.find_one({"email": session['email']})
    if not user:
        return redirect(url_for('login'))

    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)