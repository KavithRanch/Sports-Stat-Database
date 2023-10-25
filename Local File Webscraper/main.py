'''
Webscraper used to cipher any data from a website
Developed by Kavith Ranchagoda
'''
from bs4 import BeautifulSoup

# Opens file and describes actions wanting to conduct and naming the info html_file
with open('tester1.html', 'r') as html_file:
    content = html_file.read()
    print(content + "\n ------------------\n")

    soup = BeautifulSoup(content, 'lxml')  # Storing parsed version of content
    a_tags = soup.find_all('a')  # Storing all 'a' tags
    for link_titles in a_tags:  # Iterating through tags and print out text value
        print(link_titles.text)
