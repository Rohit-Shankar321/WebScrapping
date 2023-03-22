#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv


# In[44]:


source = requests.get('https://ticker.finology.in').text
soup = BeautifulSoup(source,'lxml')
#print(soup.prettify())
table = soup.find('table',class_='table table-sm table-hover screenertable')
#print(table)

titles = table.find_all('th')
#print(titles)

header =[]

for i in titles:
    name = i.text
    header.append(name)

#print(header)


df = pd.DataFrame(columns = header)

rows = table.find_all('tr')
#print(rows)

for i in rows[1:]:
    data = i.find_all('td')
    #print(data)

    row = [tr.text for tr in data]
    print(row)
    


# In[59]:


source = requests.get('https://ticker.finology.in').text
soup = BeautifulSoup(source,'lxml')
#print(soup.prettify())
table = soup.find('table',class_='table table-sm table-hover screenertable')
#print(table)

titles = table.find_all('th')
#print(titles)

header =[]
   
for i in titles:
    name = i.text
    header.append(name)

#print(header)


df = pd.DataFrame(columns = header)

rows = table.find_all('tr')
#print(rows)

for i in rows[1:]:
    #first_td = i.find_all('td')[0].find('a',class_='complink').text.strip()
    data = i.find_all('td')
    #print(data)

    row = [tr.text for tr in data]
    #row.insert(0,first_td)
    
    #print(row)
    
    l = len(df)
    
    df.loc[l]=row
    
print(df)


# In[60]:


df.to_csv('tickerfinology.csv')


# In[ ]:




