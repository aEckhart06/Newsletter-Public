# Run this after run_newsletter.py

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(sender_email: str, reciever_email: str, html_content: str, password: str):
    subject = "AI Society Weekly Newsletter"

    text_content = MIMEText("This is a HTML email. Please use an HTML-compatible email client.", "plain") #####
    html_content = MIMEText(html_content, "html")

    message = MIMEMultipart("alternative")
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = reciever_email

    message.attach(text_content) # This needs to be changed to the actual plain text version of the content
    message.attach(html_content)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password) # CHANGE FOR NEW EMAIL
        server.send_message(message)


def __main__(categories: list):
    working_path = os.getcwd()
    sender_email = "age121075@gmail.com" # Switch to the terry email
    reciever_email = "andrew.eckhart6@gmail.com"
    for category in categories:

        try:
            with open(f"{working_path}/newsletters/{category}_newsletter.html", "r") as file:
                html_content = file.read()
                
                send_email(sender_email, reciever_email, html_content, "aaxqvpxbvbrnmdzh")
                print(f"An email covering the latest in {category} has been sent to {reciever_email}!")
        except Exception as e:
            print(e)
            print(f"No newsletter found for {category}")
            continue


if __name__ == "__main__":
    # CHANGE THE CATEGIES TO THE ONES IN THE NEWSLETTERS FOLDER
    #__main__(["finance", "tech", "job market", "stock market", "management", "health care"])

    category = "tech"
    working_path = os.getcwd()
    sender_email = "age121075@gmail.com" # Switch to the terry email
    reciever_email = "andrew.eckhart6@gmail.com"
    try:
        with open(f"{working_path}/newsletters/{category}_newsletter.html", "r") as file:
            html_content = file.read()
            
            send_email(sender_email, reciever_email, html_content, "aaxqvpxbvbrnmdzh")
            print(f"An email covering the latest in {category} has been sent to {reciever_email}!")
    except Exception as e:
        print(e)
        print(f"No newsletter found for {category}")
