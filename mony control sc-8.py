import requests
from bs4 import BeautifulSoup

url = 'https://www.moneycontrol.com/'

resp = requests.get(url).content

soup = BeautifulSoup(resp, 'html.parser')


# print(soup)
def news_section():
    news = soup.find_all('h1', class_='mob-hide')
    for main_news in news:
        print(main_news.text)
        link = main_news.find('a')
        print('more at :', link.get('href'))
    sub_headlines = soup.find_all('div', class_='clearfix ltsnewsbx')
    K = 1
    for sub_headline in sub_headlines:
        print(K, sub_headline.text)
        try:
            sub = sub_headline.find('a')
            link = sub.get('href')
            print(sub.text)
            print(link)
            K += 1
            if K == 2:
                break
        except:
            print('none')
            pass


news_section()


def infoindecss():
    mkt_indexs = soup.find_all('thead')
    k = 1
    for inde in mkt_indexs:
        table = inde.find('tr')
        print(k, table.text)
        k += 1
        if k == 2:
            break
    mkts_indexs = soup.find_all('tr')
    k = 1
    for indexss in mkts_indexs:
        # print(k,indexss.text)

        try:
            nmes_indexs = indexss.find('td')
            print(k, nmes_indexs.text)
            indces_count = indexss.find('b')
            print(indces_count.text)
            price_change = indexss.find('td', width='55')
            print(price_change.text)
            price_diff = indexss.find('td', width='50')
            print(price_diff.text)
            k += 1
        except:
            pass


'''
user_dc = input()
if user_dc == '1':

    news_section()
elif user_dc == 2:
    infoindecss()
'''
