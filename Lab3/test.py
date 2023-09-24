import requests as r
from bs4 import BeautifulSoup
import time
import random as rand

url = "http://drd.ba.ttu.edu/sites/imbadproducts/"
highint = 10
lowint = 5

res = r.get(url)

soup = BeautifulSoup(res.text, 'lxml')
product_list = soup.find('div', attrs={'id':'searchresults'}).find_all('a')


for p in product_list:
    product_child = r.get(url + p['href'])
    childsoup = BeautifulSoup(product_child.content, 'lxml')
    rev = childsoup.find('div', attrs={'id': 'userreviews'}).find_all('div', attrs={'class': 'review'})
    print(rev[0])
"""
for p in product_list:
    print(url + p['href'])
    product_child = r.get(url + p['href'])
    childsoup = BeautifulSoup(product_child.content, 'lxml')
    rev = childsoup.find('div', attrs= {'id': 'userreviews'}).find_all('div', attrs= {'class': 'review'})
"""