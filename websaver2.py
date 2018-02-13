import requests
from bs4 import BeautifulSoup
from time import sleep

def trade_spider(max_pages):
  page = 1
  while page <= max_pages:
    url = 'https://www.caisoft.com/' + str(page)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
   # for link in soup.findAll('div', {'class': 'mole-news-blog-title'}): 
    for link in soup.findAll('a'): 
      href = link.get('href')
      title = link.string
      print(title)
      print(href)
      print("\n")
      sleep(0.1)
    page += 1

trade_spider(2)
  
