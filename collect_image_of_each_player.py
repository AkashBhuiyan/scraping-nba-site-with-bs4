#nba-player-header__item nba-player-header__headshot

from selenium import webdriver
from bs4 import BeautifulSoup
import requests


driver = webdriver.PhantomJS(executable_path=r'/home/akash/web_scraping/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

url = 'http://www.nba.com/players/alex/abrines/203518'

driver.get(url)

#print(driver.page_source)
soup = BeautifulSoup(driver.page_source, 'lxml')
section = soup.find('section', class_='nba-player-header__item nba-player-header__headshot')

img = section.find('img')

link = 'http:' + img['src']

print(link)

f = open('alex.jpg', 'wb')
f.write(requests.get(link).content)

f.close()

driver.quit()
