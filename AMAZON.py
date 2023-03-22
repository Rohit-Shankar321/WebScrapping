#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import requests
from bs4 import BeautifulSoup
import time
import datetime
import pandas as pd


# In[2]:


url = "https://www.amazon.in/ASUS-Zenbook-OLED-35-56-2-8K/dp/B09YHCYMD4/ref=sr_1_2_sspa?crid=1R5WWHUFG55BO&keywords=i7%2B12th%2Bgeneration%2Blaptops%2Bunder%2B200000&qid=1679153479&sprefix=%2Caps%2C328&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
#very important link
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","Accept-Encoding": "gzip, deflate, br","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "DNT":"1", "Connection":"Close", "Upgrade-Insecure-Requests":"1" }
page = requests.get(url,headers =headers)
soup = BeautifulSoup(page.content,"html.parser")
print(soup.prettify())


# In[3]:


title = soup.find(id = 'productTitle').text
print(title)


# In[4]:


price = soup.find('span', class_='a-price-whole').text
print(price)


# In[5]:


ratings = soup.find(id = 'acrCustomerReviewText').text
print(ratings)


# In[6]:


title.strip()


# In[7]:


price.strip()


# In[8]:


ratings.strip()


# In[9]:


import datetime              #also adding the date to the column

today = datetime.date.today()
print(today)


# In[10]:


title = title.strip()
price = price.strip()
ratings = ratings.strip()

print(title)
print('\n',price)
print('\n',ratings)
print('\n',today)


# # New method to save into a csv

# In[11]:


import csv

header = ['Title' , 'Price' , 'Ratings' , 'Date']
data = [title,price,ratings,today]

with open('AmazonOneProduct.csv','w',newline ='',encoding = 'UTF8')as f:
    writer = csv.writer(f)
    writer.writerow(header)     #for excel header
    writer.writerow(data)       #for data inside header


# # now we are appending the data to csv

# In[55]:


with open('AmazonOneProduct.csv','a+',newline ='',encoding = 'UTF8')as f:
    writer=csv.writer(f)
    writer.writerow(data)


# In[56]:


#see data is appending
import pandas as pd

df = pd.read_csv('AmazonOneProduct.csv')
print(df)


# In[ ]:





# In[ ]:





# # 2nd method to save into a csv what i used - 1st method by corey

# In[44]:


import csv
import requests
from bs4 import BeautifulSoup
import time
import datetime


url = "https://www.amazon.in/ASUS-Zenbook-OLED-35-56-2-8K/dp/B09YHCYMD4/ref=sr_1_2_sspa?crid=1R5WWHUFG55BO&keywords=i7%2B12th%2Bgeneration%2Blaptops%2Bunder%2B200000&qid=1679153479&sprefix=%2Caps%2C328&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","Accept-Encoding": "gzip, deflate, br","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "DNT":"1", "Connection":"Close", "Upgrade-Insecure-Requests":"1" }
page = requests.get(url,headers =headers)
soup = BeautifulSoup(page.content,"html.parser")

csv_file = open('AmazonintoCSV1stMEthod.csv','w',encoding = 'utf-8')

csv_writer =csv.writer(csv_file)
csv_writer.writerow(['title','price','ratings','today'])

title = soup.find(id = 'productTitle').text
price = soup.find('span', class_='a-price-whole').text
ratings = soup.find(id = 'acrCustomerReviewText').text
#printing the date also using datetime
today = datetime.date.today()

print(title.strip())           #strip is removing spaces and only prnting the text
print(price)
print(ratings)
print(today)

csv_writer.writerow([title,price,ratings,today])

csv_file.close()






# In[40]:


import pandas as pd


# In[41]:


df = pd.read_csv('AmazonintoCSV1stMEthod.csv')
print(df)


# In[ ]:




