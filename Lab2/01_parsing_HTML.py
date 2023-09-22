import requests as r
from bs4 import BeautifulSoup

urltoget='http://drd.ba.ttu.edu/sites/imbadproducts/'

res=r.get(urltoget)
res.content

soup = BeautifulSoup(res.content,'lxml')

results = soup.find("a")
print(results)
print(results['href'])

results=soup.find_all("a")

for l in results:
    print(l['href'])
    
    
for l in results:
    print(l.text)
    
results = soup.find_all('span', attrs={'class':'productid'})
for l in results:
    print(l.text)
    
results = soup.find_all('span', attrs={'class':'productprice'}) 
for l in results:
    print(l.text)
    
results = soup.find('div', attrs = {'id' : 'searchresults'})
print(results)
