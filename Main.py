import cv2
import argparse
import smtplib
import keys
from ultralytics import YOLO
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="S.A.F.E.G.E.N")
    parser.add_argument(
        "--webcam-resolution",
        default=[1280, 720],
        nargs=2,
        type=int
    )
    args = parser.parse_args()
    return args

def sms():
    client = Client(keys.account_sid, keys.auth_token)
    message = client.messages.create(
    body = "Alert! From S.A.F.E.G.E.N. Fire has been detected in Camera 1. Please take necessary action. ",
    from_ =keys.twilio_no,
    to=keys.reciever_no )
    print(message.body)


def email():
    sender_email = "safegenalerts@gmail.com"
    receiver_email = "sanjay040611@gmail.com"
    subject = "Alert! From S.A.F.E.G.E.N"
    message_body = "Fire has been detected in Camera 1. Please take necessary action."
    
    email_message = MIMEMultipart()
    email_message["From"] = sender_email
    email_message["To"] = receiver_email
    email_message["Subject"] = subject
    
    email_message.attach(MIMEText(message_body, "plain"))
    
    with open("fire_alert.png", "rb") as image_file:
        image_attachment = MIMEImage(image_file.read(), name="fire_alert.png")
        email_message.attach(image_attachment)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, "raatltewaulvduuk")
            server.sendmail(sender_email, receiver_email, email_message.as_string())
            server.quit()
            print(f"Email has been sent to {receiver_email}")
        except Exception as e:
            print(f"Error sending email: {e}")

def main():
    args =parse_arguments()
    frame_width, frame_height = args.webcam_resolution
    
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,frame_height)
    
    model = YOLO("best.pt")
    
    while True:
        ret, frame = cap.read()
        
        result = model(frame)[0]
        
        cv2.imshow("S.A.F.E.G.E.N", frame)

        if(model(frame)[0]):
            #sms()
            email()
        
        if(cv2.waitKey(30) == 27):
            break

if __name__ == "__main__":
    main()
    
