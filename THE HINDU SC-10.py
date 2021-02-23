import requests
from bs4 import BeautifulSoup

url = 'https://www.thehindu.com/tag/1142-1138-1073/'

resp = requests.get(url).content

soup = BeautifulSoup(resp, 'html.parser')

e_news = soup.find('span', class_='fts-menu')
print(e_news.text)

link = []

storys = []
story_card = soup.find_all('div', class_='story-card')
k = 1
for story in story_card:
    a_tag = story.find('a')

    h3_tag = story.find('h3')

    st_card = story.text
    st_cards = storys.append(st_card)
    print(k, h3_tag.text)
    a_link = a_tag.get('href')

    tag_link = link.append(a_link)
    # print(a_tag.get('href'))
    print('see more at :', a_link)
    k += 1
    print(18 * '-------------')
