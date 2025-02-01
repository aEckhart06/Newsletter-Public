from user_info import UserInfo
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import time
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


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
    # Remove leading/trailing underscores
    filename = filename.strip('_')
    # Limit length (leaving room for .md extension)
    if len(filename) > 100:
        filename = filename[:100]
    # Add .md extension
    return filename + '.md'

def get_scores(article_data):
    # Initialize scores
    scores = {
        'finance': 0,
        'tech': 0,
        'job market': 0,
        'stock market': 0,
        'management': 0,
        'health care': 0
    }
    
    # Skip if no content
    if not article_data or article_data['content'] == '':
        return scores

    # Create scoring prompt
    scoring_prompt = """
    You are an expert at analyzing article content and determining its relevance to specific topics.
    
    For the following article, score its relevance to each category on a scale of 0-10:
    0 = Not relevant at all
    5 = Moderately relevant
    10 = Highly relevant, this is a main focus of the article

    Categories to score:
    - Finance (general financial news, economics, business finances)
    - Tech (technology, innovations, software, hardware)
    - Job Market (employment, hiring, workforce trends)
    - Stock Market (stock prices, market trends, trading)
    - Management (business leadership, company management)
    - Health Care (medical, healthcare industry, health technology)

    Title: {title}
    
    Content: {content}

    Provide only the numerical scores in this exact format:
    finance: [score]
    tech: [score]
    job_market: [score]
    stock_market: [score]
    management: [score]
    health_care: [score]
    """

    model = ChatOpenAI(temperature=0.5)
    prompt_template = ChatPromptTemplate.from_template(scoring_prompt)
    prompt = prompt_template.format(
        title=article_data['title'],
        content=article_data['content'][:4000]  # Limit content length to avoid token limits
    )
    
    try:
        response = model.invoke(prompt)
        
        # Parse the response
        for line in response.content.strip().split('\n'):
            category, score = line.split(':')
            category = category.strip()
            score = score.strip()
            
            # Map response categories to score dict keys
            category_map = {
                'finance': 'finance',
                'tech': 'tech',
                'job_market': 'job market',
                'stock_market': 'stock market',
                'management': 'management',
                'health_care': 'health care'
            }
            
            if category in category_map:
                scores[category_map[category]] = score
                
    except Exception as e:
        print(f"Error getting scores: {e}")
        
    return scores


def __main__():
    q = "ai"
    news = get_news(q)
    news = news['articles'][:5]
    
    for article in news:
        # Scrape full article content
        article_data = scrape_article(article['url'])
        if article_data['content'] != '':
            scores = get_scores(article_data)
            print(f"\n {article_data['title']} \n {scores}")
            # Write all article data to the "articles" directory
            write_article_to_md(article_data, scores)
            #print("\n", article_data)
        


if __name__ == "__main__":
    __main__()