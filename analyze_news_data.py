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

def analyze_paper(content: str, source: str, model: ChatOpenAI, interests: list[str] = None) -> str:
    chunks = split_content_for_analysis(content)
    print(f"Analyzing {source} in {len(chunks)} segments...")
    
    # Modify the combined prompt to consider interests
    interest_focus = ""
    if interests:
        interest_focus = f"""
        The reader is particularly interested in these topics: {', '.join(interests)}
        Please emphasize information related to these interests in your analysis.
        If an article has minimal relevant information about these topics, provide only a brief overview
        of the most important points related to the interests.
        """
    
    combined_prompt = f"""
    You are an expert at synthesizing information from news articles. Below are separate analyses of different segments of the same article.
    {interest_focus}
    Create a comprehensive summary that:
    1. Starts with a clear, concise overview (2-3 sentences)
    2. Consolidates all key points into organized bullet points, prioritizing information about the topics of interest
    3. Eliminates redundant information
    4. Highlights the most significant facts and implications, especially those related to the topics of interest

    Separate Analyses:
    {{analyses}}

    Please structure the final summary with:
    - Executive Summary (highlighting relevance to topics of interest)
    - Key Facts & Developments (bullet points, prioritizing relevant information)
    - Important Context & Details (bullet points)
    - Implications & Impact (bullet points)
    """
    
    # First pass: Analyze each chunk
    segment_analyses = []
    for i, chunk in enumerate(chunks, 1):
        print(f"Processing segment {i}/{len(chunks)} of {source}")
        prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
        prompt = prompt_template.format(context=chunk)
        response = model.invoke(prompt)
        segment_analyses.append(response.content)
    
    # Second pass: Combine analyses into a comprehensive summary
    prompt_template = ChatPromptTemplate.from_template(combined_prompt)
    prompt = prompt_template.format(analyses="\n\n===SEGMENT BREAK===\n\n".join(segment_analyses))
    final_analysis = model.invoke(prompt)
    
    return f"\nFinal Analysis of {source}:\n{final_analysis.content}\n{'='*50}\n"

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
    
    # If no matches found, default to finance
    return best_category if category_scores[best_category] > 0 else 'finance'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--save", action="store_true", help="Save analyses to a file")
    parser.add_argument("--interests", type=str, help="Comma-separated list of topics you're interested in")
    args = parser.parse_args()

    interests = args.interests.split(",") if args.interests else []
    
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    model = ChatOpenAI(temperature=0.7)

    # Get all documents
    results = db.get()  # Replace similarity_search with direct get
    
    # Organize documents by source and track their categories/scores
    papers = defaultdict(list)
    paper_scores = {}
    
    # Get available categories from the first document's metadata
    if results and results['metadatas']:
        available_categories = [key for key in results['metadatas'][0].keys() 
                              if key not in ['source', 'timestamp']]  # Exclude non-category metadata
        target_category = get_best_matching_category(interests)
        print(f"\nBased on your interests, analyzing articles using the '{target_category}' category")
    else:
        print("No documents found in the database")
        return

    # Organize documents and their scores
    for i, (doc_content, metadata) in enumerate(zip(results['documents'], results['metadatas'])):
        source = metadata.get('source', 'unknown')
        score = float(metadata.get(target_category, 0))  # Convert to float in case it's stored as string
        
        papers[source].append(doc_content)
        paper_scores[source] = score

    # Sort sources by their scores and take top 5
    top_sources = sorted(paper_scores.items(), key=lambda x: x[1], reverse=True)[:5]
    
    all_analyses = []
    for source, score in top_sources:
        print(f"\nProcessing {source} (Score in {target_category}: {score})...")
        full_content = "\n\n---\n\n".join(papers[source])
        analysis = analyze_paper(full_content, source, model, interests)
        all_analyses.append(analysis)
        print(analysis)

    if args.save:
        with open("research_analyses.txt", "w") as f:
            f.write("\n".join(all_analyses))
        print(f"\nAnalyses saved to research_analyses.txt")

if __name__ == "__main__":
    main()