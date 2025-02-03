from user_info import UserInfo
import smtplib

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


def send_email(sender_email: str, reciever_email: str, content: str):
    subject = "AI Society Weekly Newsletter"
    message = content
    text = f"Subject: {subject}\n\n{message}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(sender_email, "aaxqvpxbvbrnmdzh")
    server.sendmail(sender_email, reciever_email, text)

    




def __main__():
    user1 = UserInfo("Oraa", "interpersonal skills, communication, leadership", "oraa.raysoni@gmail.com")
    user2 = UserInfo("Chase", "Management Information Systems, Economics", "Chase3820@gmail.com")
    user3 = UserInfo("Kaitlyn", "Management Information Systems, Economics", "krdoyle0228@gmail.com")
    user4 = UserInfo("Priyanka", "Management Information Systems, Economics", "priyankagovani2@gmail.com")
    user5 = UserInfo("Kaveri", "Management Information Systems, Economics", "kaveri.channappa@gmail.com")
    user6 = UserInfo("Jenna", "Management Information Systems, Economics", "jennacao1350@gmail.com")

    #user6 = UserInfo("Jenna", "Management Information Systems, Economics", "andrew.eckhart6@gmail.com")

    users = [user1, user2, user3, user4, user5, user6]
    """
    for user in users:
        sender_email = "age121075@gmail.com"
        reciever_email = user.email
        interests = user.interest.split(", ")
        category = get_best_matching_category(interests)

        with open(f"/Users/drew/Desktop/Coding_Projects/AI Society NL Automation/newsletters/{category}_newsletter.md", "r") as file:
            content = file.read()
        send_email(sender_email, reciever_email, content)
        print(f"An email covering the latest in {category} has been sent to {reciever_email}!")
    """

    sender_email = "age121075@gmail.com"
    reciever_email = "andrew.eckhart6@gmail.com"
    interests = ["ai", "computer science",]
    category = get_best_matching_category(interests)
    with open(f"/Users/drew/Desktop/Coding_Projects/AI Society NL Automation/newsletters/{category}_newsletter.md", "r") as file:
            content = file.read()
            send_email(sender_email, reciever_email, content)
            print(f"An email covering the latest in {category} has been sent to {reciever_email}!")


if __name__ == "__main__":
    __main__()