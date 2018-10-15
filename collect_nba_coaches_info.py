from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path=r'/home/akash/web_scraping/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

url = 'http://www.nba.com/history/awards/coach-of-the-year'

driver.get(url)
#print(driver.page_source)

soup = BeautifulSoup(driver.page_source, 'lxml')


div = soup.find('div', class_='paragraph__text')

print(div.text)



