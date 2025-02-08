import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_html_email(sender_email, sender_password, recipient_email, subject, html_content):
    # Create the MIME object
    message = MIMEMultipart('alternative')
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email

    # Create both plain text and HTML versions of the message
    # This is a good practice for email clients that don't support HTML
    text_part = MIMEText('This is a HTML email. Please use an HTML-compatible email client.', 'plain')
    html_part = MIMEText(html_content, 'html')

    # Attach both parts
    message.attach(text_part)
    message.attach(html_part)

    # Create SMTP session
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)

# Example HTML content with styling
html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 0px;
            font-family: Arial, sans-serif;
        }
        .header {
            background-color: #4A90E2;
            color: white;
            padding: 20px;
            text-align: center;
        }
        .content {
            padding: 20px;
            background-color: #f8f9fa;
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 15px;
        }
        .footer {
            text-align: center;
            padding: 20px;
            color: #666;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Welcome!</h1>
        </div>
        <div class="content">
            <h2>Hello there,</h2>
            <p>This is a sample HTML email showing various styling possibilities:</p>
            <ul>
                <li>Custom fonts and colors</li>
                <li>Responsive layout</li>
                <li>Styled buttons and elements</li>
            </ul>
            <a href="#" class="button">Call To Action</a>
        </div>
        <div class="footer">
            <p>Company Name | Address | Contact Info</p>
        </div>
    </div>
</body>
</html>
"""

# Example usage
if __name__ == "__main__":
    sender_email = "age121075@gmail.com"
    sender_password = "aaxqvpxbvbrnmdzh"
    recipient_email = "andrew.eckhart6@gmail.com"
    subject = "This is a test for the HTML email!"
    
    send_html_email(sender_email, sender_password, recipient_email, subject, html_content)