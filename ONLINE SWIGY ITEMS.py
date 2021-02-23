import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.swiggy.com/hyderabad/south-indian-collection'
resp1 = requests.get(url)
print(resp1)

resp = resp1.content

soup = BeautifulSoup(resp, 'html.parser')
soups = soup.find_all('div', class_='_3FR5S')

names = []
items = []
reatings = []
prices = []
offers = []
k = 1
for allin in soups:
    try:
        name = allin.find('div', class_='nA6kb')
        # print(k, '', 'name of restaurant :', name.text.strip())
        names.append(name)

        item = allin.find('div', class_='_1gURR')
        # print('all items:', item.text)
        items.append(item.text)
        ratings = allin.find('div', class_='_9uwBC')
        # print('ratings:', ratings.text)
        reatings.append(ratings.text)
        price = allin.find('div', class_='nVWSi')
        # print('price:', price.text)
        prices.append(price.text)
        offer = allin.find('span', class_='sNAfh')
        # print('your ofers on itms is: ', offer)
        offers.append(offer.text)
    except:

        pass

    print('------')
    k += 1
    if k == 2:
        continue
info = {'name': names, 'items': items, 'rating': reatings, 'price': prices}
data = pd.DataFrame(data=info)
print(data)
#print(data['items'])
print(data['name'].describe())

cd=data.to_csv('data.xlsx')