# Changing to csv file.

import requests
from bs4 import BeautifulSoup
import csv

source = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('TESTING-ECommerce.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['product', 'price', 'description', 'reviews', 'rating_value'])

for boxes in soup.find_all('div', class_='col-sm-4 col-lg-4 col-md-4'):
    product = boxes.div.a.text
    print(product)

    price = boxes.find('h4', class_='pull-right price').text
    print(price)

    description = boxes.find('p', class_='description').text
    print(description)

    reviews = boxes.find('p', class_='pull-right').text
    print(reviews)

    rating = boxes.find('div', class_='ratings')
    rating = rating.find('p', {'data-rating': True})
    rating_value = rating['data-rating']
    print(rating_value, 'ratings')

    print()
    csv_writer.writerow([product, price, description, reviews, rating_value])

csv_file.close()

