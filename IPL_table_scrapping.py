# removing spaces \n that are coming because of div

import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

source = requests.get(
    'https://www.iplt20.com/auction/2022#:~:text=204%20players%20were%20sold%20and,IPL)%202022%20Auction%20in%20Bengaluru.').text
soup = BeautifulSoup(source, 'lxml')

table = soup.find('table', class_='ih-td-tab auction-tbl')

title = table.find_all('th')    #getting table headers and headers are under tr i.e table row
#print(title)   #we will get a list and using for loop we will grab the data

header = []   #creating an empty list in which i will append the data of tiles one by one
for i in title:
    name = i.text
    header.append(name)
#print(header)

df = pd.DataFrame(columns = header)

rows = table.find_all('tr')

for i in rows[1:]:     #skipping 0 fist place in list bcoz it contains table headers that we already took
    first_td = i.find_all('td')[0].find('div', class_='ih-pt-ic').text.strip('\n')  # here in () default value is space but if we
    # are getting comma then specify the comma  #we are giving index 0 because it contains div tag and div tag cintains spaces

    data = i.find_all('td')[1:]

    row = [tr.text for tr in data]  #find each row data from the td which is data
    row.insert(0, first_td)

    l = len(df)
    df.loc[l] = row

print(df)

df.to_csv('ipl2022stattablescrapping.csv')
