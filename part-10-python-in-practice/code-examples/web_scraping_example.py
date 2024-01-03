# web_scraping_example.py

import requests
from bs4 import BeautifulSoup

def simple_web_scraper(url):
    """
    This function takes a URL as input and prints the titles of articles or headings found on the page.
    """
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content of the response using Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find and print titles of articles or headings (assuming they are in h2 tags)
        for heading in soup.find_all('h2'):
            print(heading.get_text().strip())
    else:
        print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")

# Example URL (You can replace this URL with any web page you wish to scrape)
example_url = 'https://example.com/'

# Call the web scraper function with the example URL
simple_web_scraper(example_url)
