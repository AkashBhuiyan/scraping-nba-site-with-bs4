# class name = small-12 columns , id = player-left-block

from selenium import webdriver
from bs4 import BeautifulSoup

#create driver
driver = webdriver.PhantomJS(executable_path=r'/home/akash/web_scraping/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

url = 'http://www.nba.com/players'


#download html page
driver.get(url)
#print(driver.page_source)

soup = BeautifulSoup(driver.page_source, 'lxml')
div = soup.find('div', {'id':'player-left-block'})
#print(div)

#get all players name
#class = row playerList
for a in div.find_all('span', class_='name-label'):
    print(a.text)


driver.quit()

