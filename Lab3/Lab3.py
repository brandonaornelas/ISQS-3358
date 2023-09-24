import requests as r
from bs4 import BeautifulSoup
import time
import random as rand
import csv

FILEPATH = "/Users/brandonornelas/ISQS-3358/Lab3/"
FILENAME = "Lab3.csv"

lowInt = 3
highInt = 8

url = "http://drd.ba.ttu.edu/isqs3358/labs/lab3/"
res = r.get(url)
soup = BeautifulSoup(res.content, 'lxml')

phone_index = soup.find('div', attrs={'id': 'phoneindex'}).find_all('a')

with open(FILEPATH + FILENAME, 'w') as Lab3:
    write = csv.writer(Lab3, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    write.writerow(['ProductID', 'Model', 'Product_Size', 'Storage', 'OS', 'Front_Camera_Features', 'Back_Camera_Features', 'Battery Capacity'])
    for phone in phone_index:
        phone_id = phone['href'].split("=")[1]
        url_res = r.get(url + phone['href'])
        phone_details = BeautifulSoup(url_res.content, 'lxml')
        phone_info = phone_details.find('div', attrs={'id': 'phoneinfo'}).find_all('span', attrs={'class': 'val'})
        write.writerow([phone_id, phone_info[0].text, phone_info[1].text, phone_info[3].text, phone_info[5].text, len(phone_info[6].find_all('li')), len(phone_info[7].find_all('li')), phone_info[8].text])
        interval = rand.randint(lowInt, highInt) + rand.random()
        print(f"Sleeping for: {interval}")
        time.sleep(interval)