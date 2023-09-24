#setup imports
import requests as r
from bs4 import BeautifulSoup
import csv

#set scrape settings variables, edit as necessasry for your environment.
urltoget='http://drd.ba.ttu.edu/isqs3358/labs/lab2/phone.php?id=1'
fp= '/home/isqsdac/Desktop/' #***NOTE****change this path to your environment
filename1 = 'dataout.csv'

#request page
res=r.get(urltoget)
 
#convert response into soup
soup = BeautifulSoup(res.content, 'lxml')

#subdivide page, by finding this div first.  Notice the extra val down in the footer we want to exclude.
phoneresult=soup.find('div', attrs={'id':'phoneinfo'})

#search the results of that div for all spans with class val (has our values)
phonevals=phoneresult.find_all('span', attrs={'class':'val'})
 
#open file handle and setup CSV writer.   
with open(fp + filename1,'w') as dataout:
    datawriter = csv.writer(dataout, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    #write header row
    datawriter.writerow(['model', 'product_size','storage', 'back_camera_features', 'front_camera_features', 'battery_capacity'])
    #write data row.  Notice the len around the next find_all to get the count of front and back camera features.
    datawriter.writerow([phonevals[0].text,
     phonevals[1].text, 
     phonevals[3].text,
     len(phonevals[7].find_all('li')),
     len(phonevals[6].find_all('li')),     
     phonevals[8].text])
                             
                             
    
  
