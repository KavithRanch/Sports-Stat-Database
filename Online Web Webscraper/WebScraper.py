'''
Online Web WebScraper
Developed by Kavith Ranchagoda

'bs4' package used for parsing/extracting HTML data
'requests' package used for requesting information from a live website
'''

from bs4 import BeautifulSoup
import requests

web_text = requests.get('https://www.on.bet365.ca/?_h=3zJEiyz5L1Tkp5tF51B1wQ%3D%3D#/HO/').text  # Extracting html text from website
web_soup = BeautifulSoup(web_text, 'lxml')  # Parsable html text
print(web_soup)