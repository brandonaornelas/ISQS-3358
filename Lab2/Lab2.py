import requests as r
from bs4 import BeautifulSoup

URL = "http://drd.ba.ttu.edu/isqs3358/labs/lab2/phone.php?id=1"

res = r.get(URL)

soup = BeautifulSoup(res.content, 'lxml')

phone_details = soup.find('div', attrs= {'id': 'PhonePrimary'})

titles = phone_details.find_all('span', attrs='title')
details = phone_details.find_all('span', attrs='val')

for i in details:
    print(i.text)