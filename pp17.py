# Use the BeautifulSoup and requests Python packages to print out a list of all 
# the article titles on the New York Times homepage.
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.practicepython.org')
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
navbar = soup.body.find('ul')
navlinks = navbar.find_all('a')
for a in navlinks:
    print(a.string)