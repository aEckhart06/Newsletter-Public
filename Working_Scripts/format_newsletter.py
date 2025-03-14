import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import json
import base64
from bs4 import BeautifulSoup
from PIL import Image
import io

class NewsletterFormatter():
    
    def create_newsletter(self, category, welcome:bool=False):
        
        
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
                    "content": "Write a semi-detailed summary of the main developments here"
                }},
                "key_updates": {{
                    "title": "Key Updates",
                    "content": "List 5-7 of the key updates here and separate each update with a new line"
                }},
                "impact": {{
                    "title": "Impact & Implications",
                    "content": "Discuss the impacts in detail here"
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
        text_template = ""

        if welcome:
            with open(f"{os.getcwd()}/html_templates/welcome_newsletter.html", "r") as f:
                html_template = f.read()
            with open(f"{os.getcwd()}/txt_templates/welcome_newsletter.txt", "r") as f:
                text_template = f.read()
        else:
            with open(f"{os.getcwd()}/html_templates/newsletter.html", "r") as f:
                html_template = f.read()
            with open(f"{os.getcwd()}/txt_templates/newsletter.txt", "r") as f:
                text_template = f.read()

        # Create a new BeautifulSoup object with the updated HTML
        soup = BeautifulSoup(html_template, 'html.parser')
        
        # Replace section contents
        sections = newsletter_data["sections"]
        
        # Find all h2 elements that contain the section titles
        h2_elements = soup.find_all('h2')
        
        # Process text content replacements
        text_content = text_template
        
        # Replace Latest Developments section
        for h2 in h2_elements:
            if "The Latest Developments in" in h2.text:
                h2.string = sections["latest_developments"]["title"]
                # Find the next paragraph and replace its content
                next_p = h2.find_next('p')
                if next_p and "Your content here" in next_p.text:
                    next_p.string = sections["latest_developments"]["content"]
                    
                # Update text content
                text_content = text_content.replace(
                    'The Latest Developments in',
                    sections["latest_developments"]["title"]
                )
                text_content = text_content.replace(
                    'Your content here <1>',
                    sections["latest_developments"]["content"]
                )
                break
                
        # Replace Key Updates section
        for h2 in h2_elements:
            if "Key Updates" in h2.text:
                if "title" in sections["key_updates"]:
                    h2.string = sections["key_updates"]["title"]
                # Find the next paragraph and replace its content
                next_p = h2.find_next('p')
                if next_p and "Your content here" in next_p.text:
                    # Clear the paragraph's content
                    next_p.clear()
                    
                    # Split the content by newlines and add each as a separate element with breaks
                    updates = sections["key_updates"]["content"].split('\n')
                    for i, update in enumerate(updates):
                        # Add the update text
                        next_p.append(update.strip())
                        # Add a line break after each update except the last one
                        if i < len(updates) - 1:
                            next_p.append(soup.new_tag('br'))
                    
                # Update text content
                text_content = text_content.replace(
                    'Key Updates',
                    sections["key_updates"].get("title", "Key Updates")
                )
                text_content = text_content.replace(
                    'Your content here <2>',
                    sections["key_updates"]["content"]
                )
                break
                
        # Replace Impact & Implications section
        for h2 in h2_elements:
            if "Impact & Implications" in h2.text:
                if "title" in sections["impact"]:
                    h2.string = sections["impact"]["title"]
                # Find the next paragraph and replace its content
                next_p = h2.find_next('p')
                if next_p and "Your content here" in next_p.text:
                    next_p.string = sections["impact"]["content"]
                    
                # Update text content
                text_content = text_content.replace(
                    'Impact & Implications',
                    sections["impact"].get("title", "Impact & Implications")
                )
                text_content = text_content.replace(
                    'Your content here <3>',
                    sections["impact"]["content"]
                )
                break
                
        # Replace Further Reading section
        for h2 in h2_elements:
            if "Further Reading" in h2.text:
                if "title" in sections["further_reading"]:
                    h2.string = sections["further_reading"]["title"]
                # Find the next paragraph and replace it with links
                next_p = h2.find_next('p')
                if next_p and "Your content here" in next_p.text:
                    # Create a new div for links
                    links_div = soup.new_tag('div')
                    links_div['style'] = "padding: 0 20px;"
                    
                    # Add each URL as a link
                    for url in sections["further_reading"]["urls"]:
                        link = soup.new_tag('a', href=url)
                        link['style'] = "font-family: 'Lora', Georgia, 'Times New Roman', Times, serif; font-size: 16px; line-height: 1.6; color: #0066cc; text-decoration: underline; margin-bottom: 10px; display: block;"
                        link.string = url
                        links_div.append(link)
                        # Add a line break between links
                        if url != sections["further_reading"]["urls"][-1]:
                            links_div.append(soup.new_tag('br'))
                    
                    # Replace the paragraph with our new links div
                    next_p.replace_with(links_div)
                    
                # Update text content
                text_content = text_content.replace(
                    'Your content here <4>',
                    "\n\n".join([f'{url}' for url in sections["further_reading"]["urls"]])
                )
                break
        
        # Convert back to HTML string
        html_content = str(soup)
        
        # Save the generated newsletter
        newsletter_path = f"{os.getcwd()}/newsletters/{category}_newsletter.html"
        os.makedirs(os.path.dirname(newsletter_path), exist_ok=True)
        newsletter_path_txt = f"{os.getcwd()}/newsletters/{category}_newsletter.txt"
        newsletter_path_html = newsletter_path
        
        with open(newsletter_path_html, "w") as f:
            f.write(html_content)
        with open(newsletter_path_txt, "w") as f:
            f.write(text_content)
        
    # Not currently in use.
    def image_to_base64(self, image_path):
        try:
            from PIL import Image
            import io

            # Open the image
            img = Image.open(image_path)
            
            # Resize to a very small size (Gmail has strict limits)
            # Making it smaller increases chances it will display
            max_size = (120, 120)  # Reduced size for better email compatibility
            img.thumbnail(max_size, Image.LANCZOS)
            
            # Convert to PNG with maximum compression
            buffer = io.BytesIO()
            img.save(buffer, format="PNG", optimize=True, compress_level=9)
            buffer.seek(0)
            
            # Get image data and encode
            img_bytes = buffer.getvalue()
            
            # Log the size for debugging
            print(f"Image size: {len(img_bytes)/1024:.2f} KB")
            
            # If still too large, further reduce quality
            if len(img_bytes) > 50000:  # 50KB is safer for Gmail
                print("Image too large, reducing size further")
                max_size = (80, 80)
                img.thumbnail(max_size, Image.LANCZOS)
                buffer = io.BytesIO()
                img.save(buffer, format="PNG", optimize=True, compress_level=9)
                buffer.seek(0)
                img_bytes = buffer.getvalue()
                print(f"Reduced image size: {len(img_bytes)/1024:.2f} KB")
            
            return base64.b64encode(img_bytes).decode('utf-8')
        except ImportError:
            # Simple fallback if PIL not available
            print("Warning: PIL not available. Using basic encoding without optimization.")
            with open(image_path, "rb") as image_file:
                img_bytes = image_file.read()
                # Log size
                print(f"Image size without PIL: {len(img_bytes)/1024:.2f} KB")
                return base64.b64encode(img_bytes).decode('utf-8')