import requests
from bs4 import BeautifulSoup

# Make a GET request to the Google News URL
url = "https://news.google.com/search?for=balneabilidade+espirito+santo&hl=pt-BR&gl=BR&ceid=BR%3Apt-419/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the news article titles in the HTML
articles_title = soup.find_all('a', {'class': 'DY5T1d RZIKme'})

# Print the article titles
for articles_title in articles_title:
    print(articles_title.text)
