import argparse
from collections import defaultdict
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter

CHROMA_PATH = "chroma"
MAX_CHUNK_SIZE = 4000  # Adjust based on your OpenAI model's context window

PROMPT_TEMPLATE = """
You are an expert at analyzing news articles and extracting key information. For the following article, provide:

1. Brief Summary (2-3 sentences)

2. Key Points:
   - List the most important facts, events, or developments
   - Include any significant numbers, statistics, or data
   - Note any major claims or conclusions

3. Important Details:
   - Key people or organizations mentioned
   - Relevant dates or timelines
   - Geographic locations (if applicable)

4. Context & Implications:
   - How this connects to broader trends or issues
   - Potential impacts or consequences

Article Content:
{context}

---

Please structure your response with clear headings and bullet points for easy reading.
"""

def split_content_for_analysis(content: str) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=MAX_CHUNK_SIZE,
        chunk_overlap=200,
        length_function=len,
    )
    return splitter.split_text(content)

def analyze_paper(content: str, url: str, model: ChatOpenAI, category: str) -> str:
    # Extract title and author from content
    title = "Untitled"
    author = "Unknown Author"
    
    # Parse content for title and author
    for line in content.split('\n'):
        if line.startswith('Title:'):
            title = line.replace('Title:', '').strip()
            break
    for line in content.split('\n'):
        if line.startswith('by '):
            author = line.replace('by ', '').strip()
            break
    
    chunks = split_content_for_analysis(content)
    #print(f"Analyzing {source} in {len(chunks)} segments...")
    
    # Modify the combined prompt to consider interests
    
    
    interest_focus = f"""
    The reader is particularly interested in the topic of: {category}
    Please emphasize information related to {category} in your analysis.
    If an article has minimal relevant information about this topic, provide only a brief overview
    of the most important points related to {category}.
    """
    
    combined_prompt = f"""
    You are an expert at synthesizing information from news articles. Below are separate analyses of different segments of the same article.
    {interest_focus}
    Create a comprehensive summary that:
    1. Starts with a clear, concise overview (2-3 sentences)
    2. Consolidates all key points into organized bullet points, prioritizing information about the topics of interest
    3. Eliminates redundant information
    4. Highlights the most significant facts and implications, especially those related to the topics of interest
    5. Is formatted with proper spacing

    Separate Analyses:
    {{analyses}}

    Please structure the final summary with:
    - Executive Summary of: {title} by {author}
    - Summary: (3-4 sentence overview of the content)
    - Key Facts & Developments (bullet points, prioritizing relevant information)
    - Important Context & Details (bullet points)
    - Implications & Impact (bullet points)
    """
    
    # First pass: Analyze each chunk
    segment_analyses = []
    for i, chunk in enumerate(chunks, 1):
        #print(f"Processing segment {i}/{len(chunks)} of {source}")
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=chunk)
        response = model.invoke(prompt)
        segment_analyses.append(response.content)
    
    # Second pass: Combine analyses into a comprehensive summary
    prompt_template = ChatPromptTemplate.from_template(combined_prompt)
    prompt = prompt_template.format(analyses="\n\n===SEGMENT BREAK===\n\n".join(segment_analyses))
    final_analysis = model.invoke(prompt)
    
    return f"\n{final_analysis.content}\n\nSource URL: {url}\n{'='*50}\n"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--save", action="store_true", help="Save analyses to a file")
    args = parser.parse_args()
    
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    model = ChatOpenAI(temperature=0.7)

    # Get all documents
    results = db.get()
    #print(results)
    if not results or not results['metadatas']:
        print("No documents found in the database")
        return

    # Hardcoded categories
    categories = ["Finance", "Tech", "Job Market", "Stock Market", "Management", "Health Care"]
    
    all_analyses = []

    
    # Process each category
    for category in categories:
        #print(f"\nAnalyzing top 2 articles for category: {category}")
        
        # Organize documents by source and track their scores for this category
        papers = defaultdict(list)
        paper_scores = {}
        
        
        for doc_content, metadata in zip(results['documents'], results['metadatas']):
            # Gets the url link to the article
            url = "unknown"
            for line in doc_content.split('\n'):
                if line.startswith('Source:'):
                    url = line.replace('Source:', '').strip()
                    break
            for line in doc_content.split('\n'):
                if line.startswith(f"{category}:"):
                    score = line.replace(f