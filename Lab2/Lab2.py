import requests as r
from bs4 import BeautifulSoup
import csv

URL = "http://drd.ba.ttu.edu/isqs3358/labs/lab2/phone.php?id=1"
FILEPATH = "C:/Users/bgorn/OneDrive/ISQS-3358/Lab2/"
FILENAME = "dataout.csv"


res = r.get(URL)

soup = BeautifulSoup(res.content, 'lxml')

phone_details = soup.find('div', attrs={'id': 'phoneinfo'})

phone_values = phone_details.find_all('span', attrs={'class': 'val'})


print(f"Model: {phone_values[0].text}")
print(f"Product Size: {phone_values[1].text}")
print(f"Storage: {phone_values[3].text}")
print(f"Back Camera Features: {len(phone_values[7].find_all('li'))}")
print(f"Front Camera Features: {len(phone_values[6].find_all('li'))}")
print(f"Battery Capacity: {phone_values[8].text}")

with open(FILEPATH + FILENAME, 'w', newline='') as dataout:
    write = csv.writer(dataout, delimiter=',', quotechar='"', quoting= csv.QUOTE_NONNUMERIC)
    write.writerow(['Model', 'Product Size', 'Storage', 'Back Camera Features', 'Front Camera Features', 'Battery Capacity'])
    write.writerow([phone_values[0].text, phone_values[1].text, phone_values[3].text, len(phone_values[7].find_all('li')), len(phone_values[6].find_all('li')), phone_values[8].text])

