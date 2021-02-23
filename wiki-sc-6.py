import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Pawan_Kalyan'
resp1 = requests.get(url)
print(resp1)
resp = requests.get(url).content
# print(resp)
soup = BeautifulSoup(resp, 'html.parser')
headlines = soup.find('h1', id='firstHeading')

print(headlines.text)

info = soup.find_all('p')
for infos in info:
    title = infos.find('a')
    print(title)
