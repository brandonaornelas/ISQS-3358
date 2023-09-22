import requests as req
from bs4 import BeautifulSoup
import time
import random as ran

url = "http://drd.ba.ttu.edu/sites/imbadproducts/"
highint = 9
lowint = 5

resparent = req.get(url)

parsoup = BeautifulSoup(resparent.text, 'lxml')
prodlist = parsoup.find('div', attrs={'id': 'searchresults'}).find_all('a')

for p in prodlist:
    print(url +p['href'])
    reschild = req.get(url +p['href'])
    childsoup = BeautifulSoup(reschild.content, 'lxml')
    rev = childsoup.find('div', attrs={'id' : 'userreviews'}).find_all('div', attrs={'class' : 'review'})
    print('prod url:  ', url +p['href'])
    print('prod_title:  ', p.find('span', attrs={'class' : 'producttitle'}).text)
    print('First Auth:  ', rev[0].find('span', attrs={'class' : 'rauthor'}).text)
    print('\n------------------\n')
    interval = ran.randint(lowint, highint) + ran.random()
    print("sleeping for:  ", interval)
    time.sleep(interval)