# Description: This script extracts ALL the latest articles from the Yahoo Finance with BeautifulSoup.

import requests
from bs4 import BeautifulSoup as soup

# Yahoo Finance news base URL
my_url = "https://finance.yahoo.com/news"


# Method Purpose: This method extracts a content dictionary from an HTML outline of the Yahoo Finance section.
# Parameter: The URL of the Yahoo Finance section.
# 1. Gets a script of all the HTML on the page.
# 2. Gets an article list - a snippet of the HTML outline including all of the articles.
# 3. Formats the list.
# 4. Concatenate the base URL with the unique article links.


def get_content_string(url):
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text

        #BeautifulSoup object to parse the HTML
        page_soup = soup(html_content, 'html.parser')

        #Find all article elements
        containers = page_soup.find_all('h3', {'class': 'Mb(5px)'})
    
        #Returns list of articles
        article_list = []
        for container in containers:
            for link in container:
                link = container.a['href']
                article_list.append(link)
                #print (article_list)

        #List above has list of lists - enumerate through and create a new list of strings
        new_list = []
        for idx, link in enumerate(article_list, start=1):
            new_list.append(link)
            #print(f"{idx}. {link}")
            #print(new_list)

        return new_list
    
    else:
        print(f"Failed to fetch content. Status code: {response.status_code}")
        return []

# Concatenates article link and base URL to get complete list of URLs at each index in the list of articles

def get_all_urls(content_string):
    url_list = []
    for i in range(len(content_string)):
        url_list.append(my_url + content_string[i])
        #print(url_list)
    return url_list

