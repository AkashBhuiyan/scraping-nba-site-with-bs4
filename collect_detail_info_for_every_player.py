# class name = small-12 columns , id = player-left-block

from selenium import webdriver
from bs4 import BeautifulSoup

class Player():
    """Doc string for player"""
    def __init__(self):
        self.name = ""
        self.link = ""
        self.age = ""
        self.born = ""

class CollectDetailInfoOfEveryPlayer:
    def load_driver(self):
        driver = webdriver.PhantomJS(executable_path=r'/home/akash/web_scraping/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

        return driver

    def collect_player_list(self):
        #create driver

        driver = self.load_driver()

        url = 'http://www.nba.com/players'


        #download html page
        driver.get(url)
        #print(driver.page_source)

        soup = BeautifulSoup(driver.page_source, 'lxml')
        div = soup.find('div', {'id': 'player-left-block'})
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
            new_player.link = "http://www.nba.com" + a['href']
            player_list.append(new_player)


        # for one_player in player_list:
        #     print(one_player.name)
        #     print(one_player.link)

        driver.quit()

        return player_list

    def collect_detail_for_each_player(self, player):
        driver = self.load_driver()
        #url = 'http://www.nba.com/players/alexis/ajinca/201582'

        driver.get(player.link)
        # print(driver.page_source)

        soup = BeautifulSoup(driver.page_source, 'lxml')
        #print(soup.prettify())
        Age = ""
        a_span = soup.find('span', string='AGE')
        #print(a_span)
        for span in a_span.findNextSibling():
            Age += span

        Born = ""
        b_span = soup.find('span', string='BORN')
        #print(b_span)
        for data in b_span.findNextSibling():
            Born += data



        player.age = Age
        player.born = Born

        driver.quit()

        return player


    def collect_detail_for_every_player(self, player_list):

        updated_player_list = []
        for player in player_list[0:3]:
        #for player in player_list:
            player_info = self.collect_detail_for_each_player(player=player)
            updated_player_list.append(player_info)
        return updated_player_list



if __name__=='__main__':

    detail_info_obj = CollectDetailInfoOfEveryPlayer()
    player_list = detail_info_obj.collect_detail_for_every_player(player_list=detail_info_obj.collect_player_list())

    for player in player_list[0:3]:
        print('name : ', player.name, ' link : ', player.link, '\n')
        print('Age : ', player.age, ' Born : ', player.born, '\n')


