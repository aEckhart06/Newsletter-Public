from User_Info import User_Info
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import time
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import openai


load_dotenv()
newsapi_api_key = os.getenv("NEWSAPI_API_KEY")


def get_news(query):
    response = requests.get(f"https://newsapi.org/v2/everything?q={query}&apiKey={newsapi_api_key}")
    return response.json()


def scrape_article(url):
    # Add headers to mimic browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Add a small delay to be respectful to servers
        time.sleep(1)
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        
        # Initialize article data
        article_data = {
            'title': '',
            'content': '',
            'author': '',
            'date': '',
            'url': url
        }
        
        # Common patterns for article content
        article_data['title'] = (
            # Try different common title patterns
            soup.find('h1') or 
            soup.find('title') or 
            soup.find(class_=['article-title', 'entry-title', 'post-title'])
        )
        if article_data['title']:
            article_data['title'] = article_data['title'].get_text().strip()
            
        # Get article content - look for common content containers
        content_tags = soup.find(
            ['article', 'main', 'div'],
            id=[ 'content', 'article-content', 'entry-content', 'post-content', 'article-body']
        )
        
        if content_tags:
            # Remove unwanted elements
            for tag in content_tags.find_all(['script', 'style', 'nav', 'header', 'footer', 'aside']):
                tag.decompose()
                
            # Extract paragraphs
            paragraphs = content_tags.find_all('p')
            article_data['content'] = '\n\n'.join(p.get_text().strip() for p in paragraphs if p.get_text().strip())
            
        return article_data
        
    except Exception as e:
        print(f"Error scraping {url}. Continuing to the next...")
        pass

def write_article_to_md(article_data, scores, output_dir="articles"):
    if not article_data:
        return
    if article_data['content'] == '':
        return
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
        
    # Use existing sanitize_filename function
    filename = sanitize_filename(article_data['title'])
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {article_data['title']}\n\n")

        if article_data['author']:
            f.write(f"Author: {article_data['author']}\n")
        else:
            print("No author found")

        if article_data['date']:
            f.write(f"Date: {article_data['date']}\n")
        else:
            print("No date found")
        f.write(f"Source: {article_data['url']}\n\n")

        # Scores for each catagory
        #
        # Finance
        f.write(f"Finance: {scores['finance']}\n")
        # New Tech
        f.write(f"Tech: {scores['tech']}\n")
        # Job Market
        f.write(f"Job Market: {scores['job market']}\n")
        # Stock Market
        f.write(f"Stock Market: {scores['stock market']}\n")
        # Management
        f.write(f"Management: {scores['management']}\n")
        # Health Care
        f.write(f"Health Care: {scores['health care']}\n\n")

        f.write(f"{article_data['content']}\n")

def sanitize_filename(title):
    # Replace invalid characters with underscores
    invalid_chars = '<>:"/\\|?*'
    # First replace spaces with underscores
    filename = title.replace(' ', '_')
    # Then replace other invalid characters
    filename = ''.join(char if char not in invalid_chars else '_' for char in filename)
    # Remove any non-ASCII characters
    filename = ''.join(char for char in filename if ord(char) < 128)
    # Remove multiple consecutive underscores
    while '__' in filename:
        filename = filename.replace('__', '_')
    # Remove leading/trailing un