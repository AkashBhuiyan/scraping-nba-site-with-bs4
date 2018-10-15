from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os
from nba import collect_detail_info_for_every_player as players_detail
import time


class CollectAllPlayerImages:


    def collect_all_player_images(self, player_list):

        for player in player_list:
            self.collect_nba_player_image(player.link, player.name)



    def collect_nba_player_image(self, url, player_name):

        driver = webdriver.PhantomJS(executable_path=r'/home/akash/web_scraping/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')

        if not os.path.exists('nba_player_img'):
            os.makedirs('nba_player_img')

        #url = 'http://www.nba.com/players/alex/abrines/203518'


        driver.get(url)

        time.sleep(2) # it will delay each request for 2 second

        #print(driver.page_source)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        section = soup.find('section', class_='nba-player-header__item nba-player-header__headshot')

        img = section.find('img')

        link = 'http:' + img['src']

        print(link)

        f = open('nba_player_img/'+'{0}.jpg'.format(player_name), 'wb')
        f.write(requests.get(link).content)

        f.close()

        driver.quit()


if __name__=='__main__':

    #collect player's details list
    detail_info_obj = players_detail.CollectDetailInfoOfEveryPlayer()
    player_list = detail_info_obj.collect_detail_for_every_player(player_list=detail_info_obj.collect_player_list())

    all_player_img_obj = CollectAllPlayerImages()
    all_player_img_obj.collect_all_player_images(player_list=player_list)


