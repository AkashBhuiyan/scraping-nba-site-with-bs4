# class name = small-12 columns , id = player-left-block

from selenium import webdriver
from bs4 import BeautifulSoup

class Player():
    """Doc string for player"""
    def __init__(self):
        self.name = ""
        self.link = ""


def collect_player_list():
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
    # for span in div.find_all('span', class_='name-label'):
    #     print(span.text)


    player_list = []

    for a in div.find_all('a'):
        span = a.find('span')
        # print('player name :', span.text)
        # print('link :', a['href'])  # find the link.

        new_player = Player()
        new_player.name = span.text
        new_player.link = "http://www.nba.com/players" + a['href']
        player_list.append(new_player)


    for one_player in player_list:
        print(one_player.name)
        print(one_player.link)

    driver.quit()

    return player_list


if __name__=='__main__':
    collect_player_list()

