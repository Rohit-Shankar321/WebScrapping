#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv


# In[29]:


#source = requests.get('https://www.flipkart.com/search?q=mobiles+under+100000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1')
#print(source)    #with this it is clear that we will get our html


# # This program contains exception handling issue , when i am scrapping multiple pages then the outout count is less than actual counting. When I am increasing the range to 20 ,30 or 50 then its not converting into csv also. For minimum number of pages its converting into csv but not geeting the csv for more pages

# In[33]:



for i in range(2,5):
    
    source = requests.get('https://www.flipkart.com/search?q=mobiles+under+100000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page= '+str(i)).text
    soup = BeautifulSoup(source,'lxml')

    csv_file = open('Flipkart-FirstPage1stMethod.csv','w' , encoding = "utf-8")      #after sepcifying it is running

    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['product','price', 'description', 'stars' , 'rating_reviews'])


    for boxes in soup.find_all('div',class_='_2kHMtA'):

        product = boxes.find('div',class_='_4rR01T').text
        print(product)

        price = boxes.find('div',class_='_30jeq3').text
        print(price)

        description = boxes.find('ul',class_='_1xgFaf').text
        print(description)

        try:
            stars = boxes.find('div',class_='_3LWZlK').text
            rating_reviews = boxes.find('span', class_='_2_R_DZ').text

        except Exception as e:
            stars = None

        print(stars)
        print(rating_reviews)



        print()
        csv_writer.writerow([product ,price, description, stars , rating_reviews])

    csv_file.close()

print('Successfully Created')   
    
    
    
#in my project i am facing an issue with exception handling that the data us not completely going to the csv, only 24 data
# is going even i am taking 10 ,20 or whatever count of pages i am giving



    
    

    
    
    
    
    
    
    
    
    
    
    
    
    


#while True:          #getting 2,1,2,1 link
    #np=soup.find('a', class_='_1LKTO3').get('href')
    #cnp = 'https://www.flipkart.com'+np
    #print(cnp)
#when we have differnet types of links pages then below code will help
    #url = cnp
    #source = requests.get(url)
    #soup = BeautifulSoup(source.text,'lxml')


# # .....................FINAL PROJECT CODE FOR SCRAPPING OF THE MULTIPLE PAGES OF FLIPKART USING 1st METHOD and IF ELSE . WORKING PROPERLY FOR ALL PAGES     ....................

# In[31]:


import requests
from bs4 import BeautifulSoup
import csv

csv_file = open('FlipkartScrappingProject.csv', 'w', encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['product', 'description', 'price', 'stars', 'rating_reviews'])

for i in range(2,5):
    source = requests.get('https://www.flipkart.com/search?q=mobiles+under+100000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=' + str(i)).text
    soup = BeautifulSoup(source, 'lxml')

    for boxes in soup.find_all('div', class_='_2kHMtA'):
        product_elem = boxes.find('div', class_='_4rR01T')
        if product_elem is not None:
            product = product_elem.text
        else:
            product = ''
        print(product)

        description_elem = boxes.find('ul', class_='_1xgFaf')
        if description_elem is not None:
            description = description_elem.text
        else:
            description = ''
        print(description)

        price_elem = boxes.find('div', class_='_30jeq3')
        if price_elem is not None:
            price = price_elem.text
        else:
            price = ''
        print(price)
        
        stars_elem = boxes.find('div', class_='_3LWZlK')
        if stars_elem is not None:
            stars = stars_elem.text
        else:
            stars = ''
        print(stars)
        
        rating_reviews_elem = boxes.find('span', class_='_2_R_DZ')
        if rating_reviews_elem is not None:
            rating_reviews = rating_reviews_elem.text
        else:
            rating_reviews = ''
        print(rating_reviews)
        
        
        print()

        csv_writer.writerow([product, description, price, stars, rating_reviews])

csv_file.close()

print('Successfully Created')


# In[ ]:




