import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

def send_email():
    # Set your email credentials
    sender_email = "your_email@email.com"
    receiver_email = "recipient_email@example.com"
    password = "your_email_password"  # Use an application-specific password if 2-factor authentication is enabled

    # Create the email content
    subject = "Daily Report"
    body = "This is your daily report email."

    # Create the MIME object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach the body to the email
    message.attach(MIMEText(body, "plain"))

    # Establish a connection with the SMTP server (in this case, Gmail)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Use TLS for security
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent successfully.")

# Schedule the email to be sent daily at a specific time (adjust as needed)
schedule.every().day.at("08:00").do(send_email)

# Keep the script running to allow scheduled tasks to be executed
while True:
    schedule.run_pending()
    time.sleep(1)
