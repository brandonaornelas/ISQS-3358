import requests as r
from bs4 import BeautifulSoup
import time
import random as rand
import csv

url = "http://drd.ba.ttu.edu/isqs3358/hw/hw1/"
res = r.get(url)
soup = BeautifulSoup(res.content, 'lxml')

userIndex = soup.find('div', attrs={'id': 'UsrIndex'}).find_all('a')

for user in userIndex:
    user_id = user['href'].split('=')[1]
    user_info = r.get(url + user['href'])
    user_details = BeautifulSoup(user_info.content, 'lxml')
    print(user_details.text)
