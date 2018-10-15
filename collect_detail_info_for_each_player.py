# Age
# Previously

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path=r'/home/akash/web_scraping/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

url = 'http://www.nba.com/players/alexis/ajinca/201582'

driver.get(url)
#print(driver.page_source)

soup = BeautifulSoup(driver.page_source, 'lxml')

Age = ""
a_span = soup.find('span', string='AGE')
for span in a_span.findNextSibling():
    Age +=span

Previously = ""
p_span = soup.find('span', string='PREVIOUSLY')
for data in p_span.findNextSibling():
    Previously+=data.text +", "

#print(content_span)


print(Age)
print(Previously)
