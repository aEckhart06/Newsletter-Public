import os
import requests
import json
from typing import Dict, List, Union
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

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

    #Review this funciton DOES NOT WORK
def get_best_matching_category(major: str) -> str:
        """
        Match user interests to one of the six predefined categories:
        Finance, Tech, Job Market, Stock Market, Management, and Health Care
        """
        CATEGORIES = {
            'finance': ['finance', 'money', 'banking', 'financial', 'economy', 'economic', 'accounting', 'economics', 'accounting'],
            'tech': ['tech', 'technology', 'software', 'digital', 'ai', 'computing', 'cyber', 'engineering', 'data', 'science', 'artificial intelligence', 'marketing', 'computer'],
            'job market': ['job', 'employment', 'hiring', 'workforce', 'career', 'labor'],
            'stock market': ['stock', 'shares', 'trading', 'market', 'investment', 'investor'],
            'management': ['management', 'leadership', 'business', 'strategy', 'executive'],
            'health care': ['health', 'healthcare', 'medical', 'medicine', 'hospital', 'clinical', 'psychology', 'bio', 'biology']
        }
        
        # Default to finance if no interests specified
        if not major:
            return 'tech'
        
        # Count matches for each category
        category_scores = {category: 0 for category in CATEGORIES}
        
       
        for category, keywords in CATEGORIES.items():
            if major in keywords or any(keyword in major for keyword in keywords):
                category_scores[category] += 1
        
        # Get category with highest score
        best_category = max(category_scores.items(), key=lambda x: x[1])[0]
        
        # If no matches found, default to tech
        return best_category if category_scores[best_category] > 0 else 'tech'

def send_email(sender_email: str, reciever_email: str,text_content: str, html_content: str, password: str, receiver_name: str = "", major: str = "", welcome: bool = False):

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
        server.login(sender_email, password) # CHANGE FOR NEW EMAIL
        server.send_message(message)

def main(sender_email: str, password: str = os.getenv("GOOGLE_APP_PASSWORD"), welcome: bool=False):
    working_path = os.getcwd()
    sheet_json_url = os.getenv("MEMBER_SHEET_URL")
    try:
        data = fetch_json(sheet_json_url) # data is a list of dictionaries containing the data for each user
    except:
        print("There was an error accessing the google sheet. Please verify accessibility and credentials.")
    for person in data:
        receiver_name = person['Full Name']
        receiver_name = receiver_name.split(" ")[0]
        receiver_name = receiver_name.capitalize()

        receiver_email = person['School Email']
        major = person['Major'].lower()
        category = get_best_matching_category(major)
        

        with open(f"{working_path}/newsletters/{category}_newsletter.html", "r") as file:
            html_content = file.read()
        with open(f"{working_path}/newsletters/{category}_newsletter.txt", "r") as file:
            text_content = file.read()
        
        send_email(sender_email, receiver_email, text_content, html_content, password, receiver_name, major, welcome)
        print(f"An email covering the latest in {category} has been sent to {receiver_email}!")
        


if __name__ == "__main__":
    main(sender_email=os.getenv("SENDER_EMAIL"), welcome=False)
