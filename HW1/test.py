import requests as r
from bs4 import BeautifulSoup
import time
import random as rand
import csv

url = "http://drd.ba.ttu.edu/isqs3358/hw/hw1/"
res = r.get(url)
soup = BeautifulSoup(res.content, 'lxml')
"""
userIndex = soup.find('div', attrs={'id': 'UsrIndex'}).find_all('a')



for user in userIndex:
    user_id = user['href'].split('=')[1]
    user_url = r.get(url + user['href'])
    user_details = BeautifulSoup(user_url.content, 'lxml')
    user_info = user_details.find('div', attrs={'id': 'userinfo'}).find_all('span', attrs={'class': 'val'})
    USER_DETAIL = user_details.find('div', attrs={'id': 'UsrDetail'}).find_all('tr')
    
    print(user_info[2].text, user_id, user_info[0].text, user_info[1].text, USER_DETAIL[1].find_all('td')[0].text, USER_DETAIL[1].find_all('td')[2].text, USER_DETAIL[1].find_all('td')[1].text, USER_DETAIL[1].find_all('td')[3].text)
"""

USER_INDEX = soup.find('div', attrs={'id': 'UsrIndex'}).find_all('a')
user_index = soup.find('div', attrs={'id': 'UsrIndex'}).find_all('tr')




for user in USER_INDEX:
    user_url = r.get(url + user['href'])
    user_info = BeautifulSoup(user_url.content, 'lxml')
    user_primary = user_info.find('div', attrs={'id': 'UsrPrimary'}).find_all('span', attrs={'class': 'val'})
    user_detail = user_info.find('div', attrs={'id': 'UsrDetail'}).find_all('tr')

    average_sleep = user_index[3].text # have to find a way to get the averages
    
    for num in range(1, 11):
        days = user_detail[num].find_all('td')[0].text
        days_water_amount = user_detail[num].find_all('td')[2].text
        sleep_hours = user_detail[num].find_all('td')[1].text
        steps = user_detail[num].find_all('td')[3].text
        user_rank = user_primary[2].text
        user_id = user['href'].split('=')[1]
        first_name = user_primary[0].text
        last_name = user_primary[1].text
        

        print(user_rank, user_id, first_name, last_name, average_sleep, days, days_water_amount, sleep_hours, steps)
    print()
    