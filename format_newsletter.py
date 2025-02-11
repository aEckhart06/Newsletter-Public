import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import re
import json
import base64

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
        newsletter_prompt = """You are an expert newsletter writer. Create a structured newsletter from the following article analyses.
        Focus on information relevant to {category}.

        The newsletter should be formatted exactly like this:
        {{
            "newsletter_title": "A catchy title for the newsletter",
            "sections": {{
                "latest_developments": {{
                    "title": "The Latest Developments in [specific area]",
                    "content": "Write the main developments here"
                }},
                "key_updates": {{
                    "title": "Key Updates",
                    "content": "List the key updates here and separate each update with a new line"
                }},
                "impact": {{
                    "title": "Impact & Implications",
                    "content": "Discuss the impacts here"
                }},
                "further_reading": {{
                    "title": "Further Reading",
                    "urls": [
                        "url1",
                        "url2",
                        "url3"
                    ]
                }}
            }}
        }}

        Analysis Content:
        {content}

        Return only the JSON structure with your content filled in. Ensure all URLs from the source content are included in the further reading section.
        """

        model = ChatOpenAI(temperature=0.7)
        prompt_template = ChatPromptTemplate.from_template(newsletter_prompt)
        response = model.invoke(prompt_template.format(category=category, content=content))
        
        # Parse the response into JSON
        try:
            newsletter_data = json.loads(response.content)
        except json.JSONDecodeError:
            print("Error parsing response into JSON")
            return None

        # Generate HTML using the template
        html_template = ""
        with open("newsletter.html", "r") as f:
            html_template = f.read()

        # Convert logo image to base64
        try:
            base64_image = self.image_to_base64("./images/AISocietyLogo.png")
            html_template = html_template.replace('src="data:image/png;base64,YOUR_BASE64_IMAGE"', 
                                               f'src="data:image/png;base64,{base64_image}"')
        except Exception as e:
            print(f"Error converting image to base64: {e}")

        # Replace placeholders with content

        html_content = html_template.replace(
            '<h2 class="newsletter-title">Newsletter Title</h2>',
            f'<h2 class="newsletter-title">{newsletter_data["newsletter_title"]}</h2>'
        )

        # Replace section contents
        sections = newsletter_data["sections"]
        html_content = html_content.replace(
            '<h2 class="section-header">The Latest Developments in</h2>\n            <p class="newsletter-text">Your content here</p>',
            f'<h2 class="section-header">{sections["latest_developments"]["title"]}</h2>\n            <p class="newsletter-text">{sections["latest_developments"]["content"]}</p>'
        )

        html_content = html_content.replace(
            '<h2 class="section-header">Key Updates</h2>\n            <pre class="newsletter-text">Your content here</pre>',
            f'<h2 class="section-header">{sections["key_updates"]["title"]}</h2>\n            <pre class="newsletter-text">{sections["key_updates"]["content"]}</pre>'
        )
        
        html_content = html_content.replace(
            '<h2 class="section-header">Impact & Implications</h2>\n            <pre class="newsletter-text">Your content here</pre>',
            f'<h2 class="section-header">{sections["impact"]["title"]}</h2>\n            <pre class="newsletter-text">{sections["impact"]["content"]}</pre>'
        )
        
        # Format URLs as links
        urls_html = "\n".join([f'<a href="{url}" class="newsletter-text">{url}</a><br>' for url in sections["further_reading"]["urls"]])
        html_content = html_content.replace(
            '<h2 class="section-header">Further Reading</h2>\n            <p class="newsletter-text">Your content here</p>',
            f'<h2 class="section-header">{sections["further_reading"]["title"]}</h2>\n            <div class="newsletter-text">{urls_html}</div>'
        )

        # Save the generated newsletter
        newsletter_path = f"{os.getcwd()}/newsletters/{category}_newsletter.html"
        os.makedirs(os.path.dirname(newsletter_path), exist_ok=True)
        
        with open(newsletter_path, "w") as f:
            f.write(html_content)
        
        return html_content

    def image_to_base64(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')