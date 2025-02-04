import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import re

class NewsletterFormatter():
    
    def create_newsletter(self, category):
        
        # Read the analysis file for the matched category
        try:
            with open(f"{os.getcwd()}/analyses/{category}.md", "r") as file:
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

        ## Further Reading
        [Include source URLs from the analysis]
        """

        model = ChatOpenAI(temperature=0.7)
        prompt_template = ChatPromptTemplate.from_template(newsletter_prompt)
        response = model.invoke(prompt_template.format())
        
        # Save the newsletter
        newsletter_path = f"{os.getcwd()}/newsletters/{category}_newsletter.md"
        os.makedirs(os.path.dirname(newsletter_path), exist_ok=True)
        
        content = response.content

        # Replace common non-ASCII characters
        content = re.sub(r'\u2019', "'", content)  # Right single quote -> Apostrophe
        content = re.sub(r'\u201C|\u201D', '"', content)  # Curly quotes -> Regular quotes
        content = re.sub(r'\u2014', '--', content)  # Em dash -> Double hyphen
        content = re.sub(r'\u2026', '...', content)  # Ellipsis -> Triple dots
        content = re.sub(r'\u2018', '`', content)

        with open(newsletter_path, "w") as f:
            f.write(content)
        
        return content