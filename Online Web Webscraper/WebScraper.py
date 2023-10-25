'''
Online Web WebScraper
Developed by Kavith Ranchagoda

'bs4' package used for parsing/extracting HTML data
'requests' package used for requesting information from a live website
'''

from bs4 import BeautifulSoup
import requests

web_text = requests.get('https://canada.sportsbook.fanduel.com/en/sports')  # Extracting html text from website
web_soup = BeautifulSoup(web_text, 'lxml')  # Parsable html text
print(web_soup)