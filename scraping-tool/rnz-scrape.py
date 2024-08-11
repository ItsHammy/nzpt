"""A tool to scrape the RNZ website for articles and save them to a file for further processing.
RNZ website: https://www.rnz.co.nz/news
Using their XML file to get the articles: https://www.rnz.co.nz/rss/political.xml
Each item contains a link to a full article, this link is then checked against the list of names of tracked politicians to see if they are mentioned in the article.
Finally, articles that mention a tracked politician are saved with a blurb to the outputs folder.
"""

# Importing the necessary libraries
from urllib.request import urlopen
import xmltodict


# List of politicians to track
politicians = ['Jacinda Ardern', 'Judith Collins', 'Winston Peters', 'James Shaw', 'David Seymour', 'Jamie Arbuckle', 'Erica Stanford']

def get_articles():
    # Open the XML file from the RNZ website
    response = urlopen('https://www.rnz.co.nz/rss/political.xml')
    xml = response.read()
    response.close()

    # Parse the XML file
    data = xmltodict.parse(xml)

    # Get the list of articles
    articles = data['rss']['channel']['item']

    # Loop through the articles and check if any of the politicians are mentioned
    for article in articles:
        title = article['title']
        link = article['link']
        description = article['description']
        pageCheck(link)

def pageCheck(url):
    content = urlopen(url).read()
    for politician in politicians:
        if politician in content:
            print('Politician mentioned:', politician)
            print('Title:', title)
            print('Link:', link)
            print('Description:', description)
            print('---')


get_articles()