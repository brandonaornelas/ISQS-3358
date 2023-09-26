import requests as r
from bs4 import BeautifulSoup
import time
import random as rand
import csv

# Defining my filepath, and filename
#FILEPATH_MAC = ""
FILEPATH_PC = "C:/Users/bgorn/OneDrive/ISQS-3358/HW1/"
FILENAME = "HW1.csv"

# Defining my low integer and high integer
HIGH_INT = 8
LOW_INT = 5

# Defining my URL to scrape, and sending HTTP GET request while parsing it with BeautifulSoup
url = "http://drd.ba.ttu.edu/isqs3358/hw/hw1/"
res = r.get(url)
soup = BeautifulSoup(res.content, 'lxml')

# This is going to be my list that will store my user information.
USER_INFORMATION = []

# Finding all the rows in the main paget
USR_ROWS  = soup.find('div', attrs={'id': 'UsrIndex'}).find_all('tr')[1:]

# Finding/Utilizing every User URL with my USR_INDEX with a for loop to be later called.
USR_INDEX = soup.find('div', attrs={'id': 'UsrIndex'}).find_all('a')
for user in USR_INDEX:
    INTERVAL = rand.randint(LOW_INT, HIGH_INT) + rand.random()
    print(f"Sleeping for: {INTERVAL}")
    time.sleep(INTERVAL) 
    USER_URL = r.get(url + user['href'])

# Looping through each row of user data in the main page
for row in USR_ROWS:
    COLUMNS = row.find_all('td')
    RANK = COLUMNS[1].text
    USER_ID = COLUMNS[0].find('a')['href'].split('=')[1]
    FIRST_NAME = COLUMNS[2].text.strip().split()[0]
    LAST_NAME = COLUMNS[2].text.strip().split()[1]
    AVERAGE_WATER = COLUMNS[4].text
    AVERAGE_SLEEP = COLUMNS[3].text
    AVERAGE_STEPS = COLUMNS[5].text
    METRIC = COLUMNS[6].text
    
    # Defining each user's URL to scrape, and sending HTTP GET request while parsing it with BeautifulSoup 
    USER_SOUP = BeautifulSoup(USER_URL.content, 'lxml')
    USER_PRIMARY = USER_SOUP.find('div', attrs={'id':'UsrPrimary'}).find_all('span', attrs={'class': 'val'})
    USER_DATA = USER_SOUP.find('div', attrs={'id': 'UsrDetail'}).find('table').find_all('tr')[1:]

    # Looping through each row in the individual user data.
    for row in USER_DATA:
        COLUMNS = row.find_all('td')
        DAYS = COLUMNS[0].text
        WATER = COLUMNS[2].text
        SLEEP = COLUMNS[1].text
        STEPS = COLUMNS[3].text
        # Appending all the user information to my empty list USER_INFORMATION
        USER_INFORMATION.append([RANK, USER_ID, FIRST_NAME, LAST_NAME, AVERAGE_WATER, AVERAGE_SLEEP, AVERAGE_STEPS, DAYS, WATER, SLEEP, STEPS, METRIC])
    

# Writing the extracted USER_INFORMATION to a csv file
with open(FILEPATH_PC + FILENAME, 'w') as HW1_DATA:
    write = csv.writer(HW1_DATA, delimiter="|", quotechar='"', quoting= csv.QUOTE_NONNUMERIC)
    write.writerow(['Rank', 'UserID', 'FirstName', 'LastName', 'AverageWater', 'AverageSleep', 'AverageStep', 'Day', 'WaterAmount', 'SleepAmount', 'StepAmount', 'Metric'])
    for row in USER_INFORMATION:
        write.writerow(row)
        