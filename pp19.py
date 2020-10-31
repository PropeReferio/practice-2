from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')n
print(soup)