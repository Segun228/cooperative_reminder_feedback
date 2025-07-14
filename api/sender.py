import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def send_email(message: str, subject = "Feedback"):
    sender_email = os.getenv("SENDER_EMAIL")
    app_password = os.getenv("EMAIL_PASSWORD")
    recipient = os.getenv("TARGET_EMAIL")


    try:
        if not sender_email or not app_password or not recipient:
                print("Invalid env fields")
                raise Exception("Invalid env fields")
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient
        msg["Subject"] = subject

        msg.attach(MIMEText(message, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
        print("✅ Email was sent successfully!")
        return "✅ Email was sent successfully!"

    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed: Check your email or app password.")
        return "❌ Authentication failed: Check your email or app password."
    except Exception as e:
        print(f"❌ Error: {e}")
        return f"❌ Error: {e}"

def main():
    message = input("Your message: ")

    result = send_email(message=message)
    print(result)

if __name__ == "__main__":
    main()