import requests
from bs4 import BeautifulSoup

names = input('enter items :')
'''P_ = int(input('from page :'))
P_2 = int(input('to page:'))'''
p_name = []
p_spcs = []
p_rating = []
p_price = []
p_link = []
p_rating1 = []

# for i in range(P_, P_2):

url = 'https://www.flipkart.com/search?q=' + names
# print('page id:', i)


def serachresults(url):
    resp = requests.get(url).content
    # print(resp)

    soup = BeautifulSoup(resp, 'html.parser')
    A_soup = soup.find_all('div', class_='_3pLy-c')
    k = 1

    for phones in A_soup:

        title = phones.find('div', class_='_4rR01T')
        p_name.append(title)
        # print(k, '--', title.text)
        try:
            review = phones.find('span', class_='_2_R_DZ')
            p_rating.append(review)
            # print(review.text)
        except:
            k = 'No ratings'
            p_rating.append(k)

            pass
        spc = phones.find('ul', class_='_1xgFaf')
        p_spcs.append(spc.text)

        # print(spc.text.replace('|', '\n'))
        price = phones.find('div', class_='_30jeq3')
        p_price.append(price.text)
        # print(price.text)
        try:
            links = phones.find('a', )

            link = links.get('href')
            p_link.append(link)
        except:
            # print('no link available ')
            p_link.append('none')
            pass
        k += 1
        print('------------------------------------------------')
    soups = soup.find_all('div', class_='_4ddWXP')
    k = 1
    for items in soups:
        titile = items.find('a', class_='s1Q9rs')
        p_name.append(titile.text)
        # print(k, '-', names, ':', titile.text)
        try:

            reviews = items.find('span', class_='_2_R_DZ')
            p_rating.append(reviews.text)
            # print('Reviews : ', reviews.text)
        except:
            print('none')
            p_rating.append('none')
            pass
        try:
            rating = items.find('div', class_='_3LWZlK')
            p_rating1.append(rating.text)

            # print('ratings:', rating.text)
        except:
            # print('Rating:none')
            p_rating1.append('none')
            pass
        price = items.find('div', class_='_30jeq3')
        # print('price:', price.text)
        p_price.append(price.text)
        lins = items.find('a', class_='_2rpwqI')
        links = url + lins.get('href')
        p_link.append(links)
        k += 1
        # print("----------------horizental----------------------")

    # print("**********************************************************")
    return p_name, p_spcs, p_rating1, p_rating, p_price, p_link


serachresults(url)
