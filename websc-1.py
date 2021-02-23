import requests
from bs4 import BeautifulSoup
from datetime import date

urll = 'https://www.indiatoday.in/'
usd = requests.get(urll).content

sd = BeautifulSoup(usd, 'html')

# print(sd.prettify())
a_tag = sd.find_all('a')
# print(a_tag.text)
"""""
l = 0
for sc in a_tag:
    print(l, sc.text)
    l += 1
    if l==288:
        break
        """
l = 1
for H3_tag in sd.find_all('h3'):
    for a_tag in H3_tag.find_all('a'):
        print(l,'-', date.today(), H3_tag.text)

        print(urll + a_tag.get('href'))
        l += 1
