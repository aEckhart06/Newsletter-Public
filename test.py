# Run this after run_newsletter.py

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()


def send_email(sender_email: str, reciever_email: str, text_content: str, html_content: str, password: str, receiver_name: str = "", major: str = "", welcome: bool = False):

    if welcome:
        # Parse HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Find and replace the NAME in the welcome message
        name_b = soup.find('b', string='NAME')
        if name_b:
            name_b.string = receiver_name

        # Find and replace MAJOR
        major_b = soup.find('b', string='MAJOR')
        if major_b:
            major_b.string = major

        # Convert back to string
        html_content = str(soup)

        # Handle plain text replacements
        text_content = text_content.replace('NAME', receiver_name)
        text_content = text_content.replace('MAJOR', major)

    subject = "AI Society Weekly Newsletter"

    text_content = MIMEText(text_content, "plain")
    html_content = MIMEText(html_content, "html")

    message = MIMEMultipart("alternative")
    message['Subject'] = subject
    message['From'] = "AI Society at Terry"
    message['To'] = reciever_email

    message.attach(text_content)
    message.attach(html_content)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(message)




if __name__ == "__main__":

    major = "MAJOR"
    category = "tech" # The catagory of news the reciever will get
    reciever_name = "NAME"
    working_path = os.getcwd()
    sender_email = os.getenv("SENDER_EMAIL") # This is the email associated with the Google App Password
    reciever_email = "age43513@uga.edu" # MODIFY 
    try:
        # This is the hardcoded filepath for the newsletter
        with open(f"{working_path}/newsletters/{category}_newsletter.html", "r") as file:
            html_content = file.read()
        with open(f"{working_path}/newsletters/{category}_newsletter.txt", "r") as file:
            text_content = file.read()

        send_email(sender_email, reciever_email, text_content, html_content, os.getenv("GOOGLE_APP_PASSWORD"), reciever_name, major, False)
        print(f"An email covering the latest in {category} has been sent to {reciever_email}!")
    except Exception as e:
        print(e)
        print(f"No newsletter found for {category}")
