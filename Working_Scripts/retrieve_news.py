from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import time
import datetime
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


load_dotenv()
newsapi_api_key = os.getenv("NEWSAPI_API_KEY")


def get_news(query):
    from_date = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
    to_date = datetime.datetime.now().strftime("%Y-%m-%d")
    response = requests.get(f"https://newsapi.org/v2/everything?q={query}&from={from_date}&to={to_date}&language=en&sortBy=popularity&apiKey={newsapi_api_key}")
    return response.json()


def scrape_article(url):
    # First try with regular requests
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'
        }
        
        time.sleep(1)
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        article_data = extract_article_data(soup, url)
        
        # If we got content, return it
        if article_data['content'].strip():
            return article_data
            
        # If no content found, try with Selenium
        return scrape_with_selenium(url)
        
    except Exception as e:
        print(f"Regular scraping failed for {url}, trying Selenium...")
        return scrape_with_selenium(url)

def scrape_with_selenium(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        
        # Wait for article content
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "article"))
        )
        
        # Get content after JavaScript execution
        selenium_soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        article_data = {
            'title': '',
            'content': '',
            'author': '',
            'date': '',
            'url': url
        }
        
        # Get title
        title = selenium_soup.find('h1')
        if title:
            article_data['title'] = title.get_text().strip()
        
        # Find the main article container
        article = selenium_soup.find('article')
        if article:
            # Get all paragraphs
            paragraphs = article.find_all('p')
            
            # Filter out ads and unwanted content
            content_paragraphs = []
            for p in paragraphs:
                text = p.get_text().strip()
                # Skip empty paragraphs or known ad content
                if not text:
                    continue
                if any(skip in text.lower() for skip in [
                    'advertisement', 
                    'most popular', 
                    'subscribe now',
                    'opens in a new window',
                    'sign up for'
                ]):
                    continue
                content_paragraphs.append(text)
            
            article_data['content'] = '\n\n'.join(content_paragraphs)
            
            # Try to find author
            author_elem = article.find(['a', 'span'], class_=['author', 'byline'])
            if author_elem:
                article_data['author'] = author_elem.get_text().strip()
            
            # Try to find date
            date_elem = article.find(['time', 'span'], class_=['date', 'published'])
            if date_elem:
                article_data['date'] = date_elem.get_text().strip()
        
        return article_data if article_data['content'] else None
        
    except Exception as e:
        print(f"Selenium scraping failed for {url}: {e}")
        return None
        
    finally:
        if 'driver' in locals():
            driver.quit()

def extract_article_data(soup, url):
    # Your existing BeautifulSoup extraction logic
    article_data = {
        'title': '',
        'content': '',
        'author': '',
        'date': '',
        'url': url
    }
    
    article_data['title'] = (
        soup.find('h1') or 
        soup.find('title') or 
        soup.find(class_=['article-title', 'entry-title', 'post-title'])
    )
    if article_data['title']:
        article_data['title'] = article_data['title'].get_text().strip()
        
    content_tags = soup.find(
        ['article', 'main', 'div'],
        id=['content', 'article-content', 'entry-content', 'post-content', 'article-body']
    )
    
    if content_tags:
        for tag in content_tags.find_all(['script', 'style', 'nav', 'header', 'footer', 'aside']):
            tag.decompose()
            
        paragraphs = content_tags.find_all('p')
        article_data['content'] = '\n\n'.join(p.get_text().strip() for p in paragraphs if p.get_text().strip())
        
    return article_data

def write_article_to_md(article_data, scores, output_dir="articles"):
    if not article_data:
        return
    if article_data['content'] == '':
        return
    
    # Create the output directory if it doesn't exist
    output_dir_path = f"{os.getcwd()}/{output_dir}"
    print(output_dir_path)
    os.makedirs(output_dir_path, exist_ok=True)
        
    # Use existing sanitize_filename function
    filename = sanitize_filename(article_data['title'])
    filepath = os.path.join(output_dir_path, filename)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"Title: {article_data['title']}\n\n")

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
        # Tech
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


def __main__(query: str="ai", num_articles: int=10, output_dir: str='articles'):
    news = get_news(query)
    news = news['articles'][:num_articles]
    length = len(news)
    print(length)
    
    no_data_counter = 0

    for i in range(length):
        # Scrape full article content
        article_data = scrape_article(news[i]['url'])
        if article_data:
            if article_data['content']:
                if article_data['content'] != '' or article_data['content'] is None:
                    scores = get_scores(article_data)
                    print(f"\n {article_data['title']} \n {scores}")
                    # Write all article data to the "articles" directory
                    write_article_to_md(article_data, scores, output_dir)
                    
                else:
                    print(f"{article_data['title']} is blocked by a paywall.")
                    no_data_counter += 1
            else:
                print(f"No content for the article: {article_data['title']}")
                no_data_counter += 1
        else:
            print("No article data")
            no_data_counter += 1
        print(f"{((i+1)/length)*100}% of articles found.")
    
    return no_data_counter



if __name__ == "__main__":
    __main__("ai")