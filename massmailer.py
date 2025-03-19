import smtplib
import ssl
from email.message import EmailMessage

def send_bulk_email(sender_email, sender_name, sender_password, subject, body, recipients_file):
    try:
        with open(recipients_file, 'r') as file:
            recipients = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("Error: The recipients file was not found.")
        return

    if not recipients:
        print("Error: No recipients found in the file.")
        return

    smtp_server = "smtp.gmail.com"
    smtp_port = 465

    context = ssl.create_default_context()
    
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, sender_password)
            
            for recipient in recipients:
                msg = EmailMessage()  
                msg['From'] = f"{sender_name} <{sender_email}>"
                msg['To'] = recipient
                msg['Subject'] = subject
                msg.set_content(body)

                server.send_message(msg)
                print(f"Email sent to {recipient}")

    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Check your email and app password.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    sender_email = input("Enter your Gmail address: ")
    sender_password = input("Enter your Gmail app password: ")
    sender_name = input("Enter sender name: ")
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")
    recipients_file = input("Enter the path to the recipients text file: ")

    send_bulk_email(sender_email, sender_name, sender_password, subject, body, recipients_file)
