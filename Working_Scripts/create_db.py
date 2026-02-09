# from langchain.document_loaders import DirectoryLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os
import shutil
import nltk
from collections import defaultdict

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


nltk.download('averaged_perceptron_tagger_eng')
nltk.download('punkt_tab')
nltk.data.path.append('/Users/andreweckhart/nltk_data') 

# Load environment variables. Assumes that project contains .env file with API keys
load_dotenv()

CHROMA_PATH = "chroma"


def generate_data_store(data_path: str):
    documents = load_documents(data_path)
    chunks = split_text(documents)
    save_to_chroma(chunks)


def load_documents(data_path: str) -> list[Document]:
    loader = DirectoryLoader(data_path, glob="*.md")
    documents = loader.load()
    return documents


def split_text(documents: list[Document]) -> list[Document]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # Increased for better context
        chunk_overlap=200,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    
    # Group chunks by source for logging
    sources = defaultdict(int)
    for chunk in chunks:
        sources[chunk.metadata.get("source", "unknown")] += 1
    
    print("\nChunks per document:")
    for source, count in sources.items():
        print(f"{source}: {count} chunks")
    
    return chunks


def save_to_chroma(chunks: list[Document]):
    # Clear out the database first.
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a new DB from the documents.
    Chroma.from_documents(
        chunks, GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", google_api_key=os.getenv("GEMINI_API_KEY")), persist_directory=CHROMA_PATH
    )
    
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")


def __main__(data_path: str=f"{os.path.dirname(os.getcwd())}/articles"):
    generate_data_store(data_path)

if __name__ == "__main__":
    __main__()
