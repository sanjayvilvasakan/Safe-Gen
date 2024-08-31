# Simple Mail Transfer Protocol Library (Build-in) 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Email configuration
sender_email = "safegenalerts@gmail.com" # Sender's Email ID
receiver_email = "sanjay040611@gmail.com" # Reciever's Email ID
subject = "Alert! From S.A.F.E.G.E.N"
message_body = "Fire has been detected in Camera 1. Please take necessary action."

# Create a MIMEText object for the email body
email_message = MIMEMultipart()
email_message["From"] = sender_email
email_message["To"] = receiver_email
email_message["Subject"] = subject

# Attach the message body
email_message.attach(MIMEText(message_body, "plain"))

# Load the PNG image attachment
with open("fire_alert.png", "rb") as image_file:
    image_attachment = MIMEImage(image_file.read(), name="fire_alert.png")
    email_message.attach(image_attachment)

# Connect to the SMTP server and send the email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, "raatltewaulvduuk")
    server.sendmail(sender_email, receiver_email, email_message.as_string())
    server.quit()
    print(f"Email has been sent to {receiver_email}")
except Exception as e:
    print(f"Error sending email: {e}")
