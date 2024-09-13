"""A tool to scrape the RNZ website for articles and save them to a file for further processing.
RNZ website: https://www.rnz.co.nz/news
Using their XML file to get the articles: https://www.rnz.co.nz/rss/political.xml
Each item contains a link to a full article, this link is then checked against the list of names of tracked politicians to see if they are mentioned in the article.
Finally, articles that mention a tracked politician are saved with a blurb to the outputs folder.
"""

# SETTINGS

PRINTER = 0 # CHANGE TO 1 TO PRINT LOGS TO CONSOLE

# Importing the necessary libraries
import urllib.request
import xmltodict
from datetime import datetime



# List of politicians to track
politicians = ['Jacinda Ardern', 'Judith Collins', 'Winston Peters', 'James Shaw', 'David Seymour', 'Jamie Arbuckle', 'Erica Stanford']

def get_articles():
    # Open the XML file from the RNZ website
    response = urllib.request.urlopen('https://www.rnz.co.nz/rss/political.xml')
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
        pageCheck(link, title, description)

def pageCheck(link, title, description):
    page = urllib.request.urlopen(link)
    if PRINTER == 1:
        print('Page opened "{}", ({})'.format(title, link))
    content = page.read().decode('utf-8')
    for politician in politicians:
        if politician in content:
            if PRINTER == 1:
                output_print('content', title, link, description, politician)
            pass
        elif politician in title:
            if PRINTER == 1:
                output_print('heading', title, link, description, politician)
            pass
        elif politician in description:
            if PRINTER == 1:
                output_print('blurb', title, link, description, politician)
            pass
    page.close()
    if PRINTER == 1:
        print('Page closed "{}", ({})'.format(title, link))
        print('\n\n')

def output_files():
    pass

def output_print(location, title, link, description, politician):
    """Prints the output to the console. Used for testing and debugging."""
    print('\nPolitician mentioned ({}):'.format(location), politician)
    print('Title:', title)
    print('Link:', link)
    print('Description:', description)
    print('---\n')

startTime = datetime.now()
get_articles()
print("File rnz-scrape.py finished in", datetime.now() - startTime)