from .format_newsletter import NewsletterFormatter

def __main__(categories: list=["finance", "tech", "job market", "stock market", "management", "health care"]):

    newsletter_formatter = NewsletterFormatter()

    for category in categories:
        newsletter_formatter.create_newsletter(category, welcome=False)
        print(f"Newsletter created for {category}")


if __name__ == "__main__":
    __main__()