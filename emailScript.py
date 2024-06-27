import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(smtpServer, port, login, password, senderEmail, recipientEmail, subject, body):
    # Create the email headers and attach the body
    msg = MIMEMultipart()
    msg['From'] = senderEmail
    msg['To'] = recipientEmail
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtpServer, port) as server:
        server.starttls()
        server.login(login, password)
        server.sendmail(senderEmail, recipientEmail, msg.as_string())

def main():
    # Read moisture.txt
    fileContent = ""
    with open("moisture.txt", 'r') as file:
        fileContent = file.read()

    # Details
    smtpServer = 'smtp.gmail.com'
    port = 587  # Port for TLS/STARTTLS
    login = os.getenv('_EMAIL_')
    password = os.getenv('_EMAIL_PASSWORD_')
    senderEmail = os.getenv('_EMAIL_')
    recipientEmail = os.getenv('_EMAIL_')
    subject = 'Plant Moisture Readings'
    body = fileContent

    # Send
    sendEmail(smtpServer, port, login, password, senderEmail, recipientEmail, subject, body)


if __name__ == "__main__":
    main()

    # Clears file after use
    with open("moisture.txt", 'w') as file:
        fileContent = file.truncate(0)