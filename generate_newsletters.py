from format_newsletter import NewsletterFormatter

def __main__():

    nl_categories = ["Finance", "Tech", "Job Market", "Stock Market", "Management", "Health Care"]
    newsletter_formatter = NewsletterFormatter()

    for category in nl_categories:
        newsletter_formatter.create_newsletter(category)
        print(f"Newsletter created for {category}")


if __name__ == "__main__":
    __main__()