import os
import shutil
from collections import defaultdict
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter

CHROMA_PATH = "chroma"
MAX_CHUNK_SIZE = 2000  # Reduced from 3000

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
    
    # Limit the number of chunks processed
    chunks = split_content_for_analysis(content)
    MAX_CHUNKS = 5  # Process only first 5 chunks
    chunks = chunks[:MAX_CHUNKS]
    
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
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=chunk)
        response = model.invoke(prompt)
        # Summarize each analysis to keep only key points
        segment_analyses.append(response.content)
    
    # Second pass: Combine analyses in smaller groups if needed
    if len(segment_analyses) > 2:
        # Process analyses in pairs to avoid token limits
        final_segments = []
        for i in range(0, len(segment_analyses), 2):
            pair = segment_analyses[i:i+2]
            prompt_template = ChatPromptTemplate.from_template(combined_prompt)
            prompt = prompt_template.format(analyses="\n\n===SEGMENT BREAK===\n\n".join(pair))
            response = model.invoke(prompt)
            final_segments.append(response.content)
        
        # Final combination if needed
        if len(final_segments) > 1:
            prompt = prompt_template.format(analyses="\n\n===SEGMENT BREAK===\n\n".join(final_segments))
            final_analysis = model.invoke(prompt)
        else:
            final_analysis = model.invoke(final_segments[0])
    else:
        # If only 1-2 segments, combine directly
        prompt_template = ChatPromptTemplate.from_template(combined_prompt)
        prompt = prompt_template.format(analyses="\n\n===SEGMENT BREAK===\n\n".join(segment_analyses))
        final_analysis = model.invoke(prompt)
    
    return f"\n{final_analysis.content}\n\nSource URL: {url}\n{'='*50}\n"

def __main__(categories: list=["Finance", "Tech", "Job Market", "Stock Market", "Management", "Health Care"], output_dir: str="analyses"):
    
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    model = ChatOpenAI(temperature=0.7)

    # Get all documents
    results = db.get()
    #print(results)
    if not results or not results['metadatas']:
        print("No documents found in the database")
        return
    
    all_analyses = []
    curr_path = os.getcwd()
    full_path_to_dir = f"{curr_path}/{output_dir}"
    # Remove output directory if it exists
    if os.path.exists(full_path_to_dir) and os.path.isdir(full_path_to_dir):
        shutil.rmtree(full_path_to_dir)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)


    
    # Process each category
    for category in categories:
        
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
                    score = line.replace(f"{category}:", "").strip()
                    score = float(score)
                    break
                else:
                    score = 0.0
            
            
            papers[url].append(doc_content)
            paper_scores[url] = score
            
        
        # Get top sources for this category
        top_sources = sorted(paper_scores.items(), key=lambda x: x[1], reverse=True)[:10] # Top 10 sources of this category

        # Analyze each top source
        for url, score in top_sources:
            full_content = "\n\n---\n\n".join(papers[url])
            analysis = analyze_paper(full_content, url, model, category)
            all_analyses.append(f"\nCategory: {category}\n{analysis}")
            print(analysis)

            

            with open(f"{os.getcwd()}/{output_dir}/{category}.md", "a") as file:
                file.write(analysis)

if __name__ == "__main__":
    __main__()
    