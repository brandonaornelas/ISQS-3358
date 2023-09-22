import requests as r
from bs4 import BeautifulSoup

res = r.get("http://drd.ba.ttu.edu/sites/imbadproducts/")

soup = BeautifulSoup(res.content, 'lxml')

results = soup.find_all('a')
for i in results:
    print(i['href'])
    print("Product ID: " + i.find('span', attrs = {"class": "productid"}).text)
    print("Product Title: " + i.find('span', attrs = {"class": "producttitle"}).text)
    print()

