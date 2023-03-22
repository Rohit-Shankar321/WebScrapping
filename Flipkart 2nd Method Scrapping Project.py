#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


# In[13]:


Product_name =[]
Prices  = []
Description = []
Reviews =[]

for i in range(2,4):
    source = requests.get('https://www.flipkart.com/search?q=mobiles+under+100000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page='+str(1)).text
    soup = BeautifulSoup(source,'lxml')
    box = soup.find('div' , class_='_1YokD2 _3Mn1Gg')

    #.................................................for product_name
    names = box.find_all('div',class_='_4rR01T')
    #print(names)

    for i in names:
        names = i.text
        Product_name.append(names)

    #print(len(Product_name))
    #print(Product_name)
    #print('\n\n')

    #.................................................for its price
    cost = box.find_all('div',class_='_30jeq3 _1_WHN1')
    #print(cost)

    for i in cost:
        cost = i.text
        Prices.append(cost)

    #print(len(Prices))
    #print(Prices)
    #print('\n\n')

    #................................................for description
    details = box.find_all('ul' , class_='_1xgFaf')
    #print(details)

    for i in details:
        details = i.text
        Description.append(details)

    #print(len(Description))    
    #print(Description)
    #print('\n\n')

    #................................................for Reviews
    opinion = box.find_all('div',class_='_3LWZlK')
    #print(opinion)

    for i in opinion:
        opinion = i.text
        Reviews.append(opinion)

    #print(len(Reviews)) #count of review coming is 39 but our product is only 24  
    #print(Reviews)
    
df =pd.DataFrame({'Product_name':Product_name , 'Prices':Prices , 'Description':Description, 'Reviews':Reviews})
print(df)

df.to_csv('EKARTscrapping2ndMethod.csv')



#showing error bcause while printing in one of the columns may be data count is low .


# # FINAL FLIPKART PROJECT USING 2ND METHOD , IF-ELSE STATEMENT AND BY EMPTY LIST CREATING

# In[22]:


import requests
from bs4 import BeautifulSoup
import csv

Product_name =[]
Prices  = []
Description = []
Stars = []
Reviews = []

for i in range(2, 5):
    url = 'https://www.flipkart.com/search?q=mobiles+under+100000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=' + str(i)
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    for boxes in soup.find_all('div', class_='_2kHMtA'):
        
        
        
        product_elem = boxes.find('div', class_='_4rR01T')       
        if product_elem is not None:
            product = product_elem.text
        else:
            product = ''
        Product_name.append(product)
        

        description_elem = boxes.find('ul', class_='_1xgFaf')
        if description_elem is not None:
            description = description_elem.text
        else:
            description = ''
        Description.append(description)
        
        

        price_elem = boxes.find('div', class_='_30jeq3')
        if price_elem is not None:
            price = price_elem.text
        else:
            price = ''
        Prices.append(price)
        
        
        
        stars_elem = boxes.find('div', class_='_3LWZlK')
        if stars_elem is not None:
            stars = stars_elem.text
        else:
            stars = ''
        Stars.append(stars)
        
        
        
        rating_reviews_elem = boxes.find('span', class_='_2_R_DZ')
        if rating_reviews_elem is not None:
            rating_reviews = rating_reviews_elem.text
        else:
            rating_reviews = ''
        Reviews.append(rating_reviews)
        
        
        


df = pd.DataFrame({'Product_Name':Product_name,'Cost':Prices,'Specifications':Description,'Ratings':Stars,'Review':Reviews})
print(df)

df.to_csv('FlipkartScrappingProject-ifelse-2ndmethod.csv')

print('Successfully Created')


# In[ ]:




