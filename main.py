from bs4 import BeautifulSoup

# Opens file and describes actions wanting to conduct and naming the info html_file
with open('tester1.html', 'r') as html_file:
    content = html_file.read()
    print(content)