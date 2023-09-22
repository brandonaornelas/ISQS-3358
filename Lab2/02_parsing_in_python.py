import requests as r
from bs4 import BeautifulSoup
import csv

#setting variables
urltoget='http://drd.ba.ttu.edu/sites/imbadproducts/'
filepath= '/home/isqsdac/Desktop/'
filename1 = 'fileout.csv'

#request
res=r.get(urltoget)

#Just a test of responsecode and headers.  not needed for parsing, more for
#debugging.  lines 15-20
if res.status_code == 200:
    print('request is good')
else:
    print('bad request, received code ' +str(res.status_code))
    
print(res.headers)

#creates soup object.  
soup = BeautifulSoup(res.content, 'lxml')

#Locate all "anchor" tags and print.  More for testing, not needed.
product_result=soup.find_all('a')
for pr in product_result:
    print(pr)
    
#Subset the webpage.    
search_results=soup.find('div', attrs={'id':'searchresults'})

#another test to show how to search within a search.
product_results=search_results.find_all('a')
for pr in product_result:
    print(pr)
    
#Example that uses line 31 to show how to print all data to console needed
#from the webpage.  Note, great method to test if you parsing routines are 
#working prior to introducting write to csv.      
product_result=search_results.find_all('a')
for pr in product_result:
    print("URL:" +pr['href'])
    print('product ID:' +pr.find('span', attrs ={'class':'productid'}).text)
    print('product title:' +pr.find('span', attrs ={'class':'producttitle'}).text)
    print('product price:' +pr.find('span', attrs ={'class':'productprice'}).text)
    print('product description:' +pr.find('span', attrs ={'class':'productdesc'}).text)
    print('-------------------------------')

    
#same as lines 42-48, execpt it has the output go to a csv file rather than the 
#console.  Note, how similar these blocks are.  Much easier to write 42-48,
#then expand into 54-62.    
with open(filepath + filename1,'w') as dataout:
    datawriter = csv.writer(dataout, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    datawriter.writerow(['URL', 'id', 'title', 'price','description'])
    for pr in product_result:
        datawriter.writerow([pr['href'],
                             pr.find('span', attrs ={'class':'productid'}).text,
                             pr.find('span', attrs ={'class':'producttitle'}).text,
                             pr.find('span', attrs ={'class':'productprice'}).text,
                             pr.find('span', attrs ={'class':'productdesc'}).text])
                             
                             
