
# The script that will do everything.

import os
import Working_Scripts.retrieve_news as retrieve_news
import Working_Scripts.create_db as create_db
import Working_Scripts.analyze_news_data as analyze_news_data 
import Working_Scripts.generate_newsletters as generate_newsletters



def __main__(query: str, num_articles: int, article_output_dir: str, categories: list):
    working_path = os.getcwd()
    
    # Address the hardcoded categories
    unscrapable_articles_num = retrieve_news.__main__(query, num_articles, article_output_dir)         # Pass a query, Pass a number of articles to be retrieved, Pass the name of the output directory for the raw article data
    print("Retrieval Complete")
    if unscrapable_articles_num == 1:
        print("There was 1 article that was unscrapable.")
    elif unscrapable_articles_num > 0:
        print(f"{unscrapable_articles_num} articles were unscrapable.")
    
    if os.path.isdir(f"{working_path}/{article_output_dir}"):
        # Address nltk downloads
        create_db.__main__(article_output_dir)               # Pass a path to the directory where all the articles are (.md)
        print("DB Created")

        analyze_news_data.__main__(categories)               # Pass a list of categories
        print("Data Analysis Complete")

        generate_newsletters.__main__(categories)            # Pass the same list of categories
        print("Newsletters Complete")




if __name__ == "__main__":
    num_of_articles_to_query_for = 50
    query = "ai"
    __main__(query, num_of_articles_to_query_for, "articles", ["finance", "tech", "job market", "stock market", "management", "health care"])
    