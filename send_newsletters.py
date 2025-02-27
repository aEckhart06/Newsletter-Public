import os
import requests
import json
from typing import Dict, List, Union
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def fetch_json(url: str) -> Union[Dict, List]:
    """
    Fetches JSON data from a URL with error handling.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        return response.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        print(f"Raw response: {response.text}")
        raise
def get_best_matching_category(interests: list[str]) -> str:
        """
        Match user interests to one of the six predefined categories:
        Finance, Tech, Job Market, Stock Market, Management, and Health Care
        """
        CATEGORIES = {
            'finance': ['finance', 'money', 'banking', 'financial', 'economy', 'economic'],
            'tech': ['tech', 'technology', 'software', 'digital', 'ai', 'computing', 'cyber'],
            'job market': ['job', 'employment', 'hiring', 'workforce', 'career', 'labor'],
            'stock market': ['stock', 'shares', 'trading', 'market', 'investment', 'investor'],
            'management': ['management', 'leadership', 'business', 'strategy', 'executive'],
            'health care': ['health', 'healthcare', 'medical', 'medicine', 'hospital', 'clinical']
        }
        
        # Default to finance if no interests specified
        if not interests:
            return 'tech'
        
        # Count matches for each category
        category_scores = {category: 0 for category in CATEGORIES}
        
        for interest in interests:
            interest = interest.lower().strip()
            for category, keywords in CATEGORIES.items():
                if interest in keywords or any(keyword in interest for keyword in keywords):
                    category_scores[category] += 1
        
        # Get category with highest score
        best_category = max(category_scores.items(), key=lambda x: x[1])[0]
        
        # If no matches found, default to tech
        return best_category if category_scores[best_category] > 0 else 'tech'

def send_email(sender_email: str, reciever_email: str, html_content: str, password: str, receiver_name: str = "", major: str = "", welcome: bool = False):

    if welcome:
        html_content = html_content.replace(
            '<p class="section-header"><b>NAME</b>, welcome to the AI Society Newsletter!</p>',
            f'<p class="section-header"><b>{receiver_name}</b>, welcome to the AI Society Newsletter!</p>'
        )
        html_content = html_content.replace(
            '<b>MAJOR</b>',
            f'<b>{major}</b>'
        )
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

def main(sender_email: str, password: str = "iiwqkbhkuazyozhf"):
    working_path = os.getcwd()
    sheet_json_url = "https://script.google.com/macros/s/AKfycbxBWORhrVBUwKrEuKRb5u7Zjzjj9Q12J5-FWfhSehG-mjspS29H4CoOgozgPJo-znti-A/exec"
    try:
        data = fetch_json(sheet_json_url) # data is a list of dictionaries containing the data for each user
    except:
        print("There was an error accessing the google sheet. Please verify accessibility and credentials.")
    for person in data:
        receiver_name = person['Full Name']
        receiver_name = receiver_name.split(" ")[0]
        receiver_name = receiver_name.capitalize()

        receiver_email = person['Personal Email']
        major = person['Major']
        category = get_best_matching_category(major)

        with open(f"{working_path}/newsletters/{category}_newsletter.html", "r") as file:
            html_content = file.read()
        
        send_email(sender_email, receiver_email, html_content, password, receiver_name, major, welcome=True)
        print(f"An email covering the latest in {category} has been sent to {receiver_email}!")


if __name__ == "__main__":

    # MUST SWITCH TO THE TERRY EMAIL
    main(sender_email="aisocietyatterry@gmail.com")
