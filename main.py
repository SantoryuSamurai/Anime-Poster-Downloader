# Import Required Module
import requests
from bs4 import BeautifulSoup
import re

# Get URL Content
r = requests.get('https://aniwatch.to/most-popular')

# Parse HTML Code
soup = BeautifulSoup(r.content, 'lxml')
anime_lists=soup.find_all('div', class_='film-poster')
images=soup.find_all('img')

for image in images:
    name = re.search("alt.*?\".*?\"",str(image))
    if name is None:
        continue
    link = re.search("src.*?\".*?\"",str(image))
    if link is None:
        continue
    print(name.group()[5:-1])
    print(link.group()[5:-1])
    print(" ")
    