"""A tool to scrape the RNZ website for articles and save them to a file for further processing.
RNZ website: https://www.rnz.co.nz/news
Using their XML file to get the articles: https://www.rnz.co.nz/rss/political.xml
Each item contains a link to a full article, this link is then checked against the list of names of tracked politicians to see if they are mentioned in the article.
Finally, articles that mention a tracked politician are saved with a blurb to the outputs folder.
"""

# Importing the necessary libraries
import urllib2
import xmltodict

def get_articles():
    # Open the XML file from the RNZ website
    response = urllib2.urlopen('https://www.rnz.co.nz/rss/political.xml')
    xml = response.read()
    response.close()

    # Parse the XML file
    data = xmltodict.parse(xml)

    # Get the list of articles
    articles = data['rss']['channel']['item']

    # List of politicians to track
    politicians = ['Jacinda Ardern', 'Judith Collins', 'Winston Peters', 'James Shaw', 'David Seymour']

    # Loop through the articles and check if any of the politicians are mentioned
    for article in articles:
        title = article['title']
        link = article['link']
        description = article['description']

        for politician in politicians:
            if politician in title or politician in description:
                print('Politician mentioned:', politician)
                print('Title:', title)
                print('Link:', link)
                print('Description:', description)
                print('---')