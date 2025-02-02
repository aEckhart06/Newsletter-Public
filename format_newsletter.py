from user_info import UserInfo
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import re

class NewsletterFormatter():
    
    def create_newsletter(self, category):
        
        # Read the analysis file for the matched category
        try:
            with open(f"/Users/drew/Desktop/Coding_Projects/AI Society NL Automation/analyses/{category}.md", "r") as file:
                content = file.read()
        except FileNotFoundError:
            print(f"No analysis file found for category: {category}")
            return None

        # Create newsletter prompt
        newsletter_prompt = f"""
        You are an expert newsletter writer. Create a concise, engaging newsletter from the following article analyses.
        Focus on information relevant to {category}.

        The newsletter should:
        1. Have a catchy title
        2. Start with a brief introduction (2-3 sentences)
        3. Present the most important developments in bullet points
        4. Include relevant statistics or data if available
        5. End with key takeaways or implications
        6. Be written in a professional but engaging tone
        7. Be formatted with clear sections and spacing

        Analysis Content:
        {content}

        Format the newsletter with these sections:
        # [Newsletter Title]
        
        ## Latest Developments in {category}
        [Introduction]

        ## Key Updates
        [Bullet points of important information]

        ## Impact & Implications
        [Brief discussion of significance]

        ## Further Readi