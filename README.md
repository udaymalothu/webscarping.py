import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.flipkart.com/mobiles/~cs-fdeu9sdw9c/pr?sid=tyy%2C4io&collection-tab-name=Iphone+SE+2020&sort=price_asc&otracker=clp_banner_1_8.bannerX3.BANNER_mobile-phones-big-saving-days-jan-21-9399-933f-store_BOCUARSE2Y69&fm=neo%2Fmerchandising&iid=M_78a0b44b-8b6f-486f-81d2-49f9290a64e6_8.BOCUARSE2Y69&ppt=clp&ppn=mobile-phones-big-saving-days-jan-21-9399-933f-store&ssid=fgq939knhc0000001611038771337'

# url = 'https://www.flipkart.com/kemei-km-632-runtime-45-min-trimmer-men/p/itmf7d4502b24b94?pid=TMRFNH6ZQXPXSG3H&lid=LSTTMRFNH6ZQXPXSG3HVDCHPI&marketplace=FLIPKART&fm=personalisedRecommendation%2Fp2p-same&iid=R%3As%3Bp%3ATMRFTXPFNZHDGF5T%3Bpt%3Ahp%3Buid%3Af4f29482-5892-11eb-9f86-554a742b6a02%3B.TMRFNH6ZQXPXSG3H&ppt=hp&ppn=homepage&ssid=tsswx9oheo0000001610867378941&otracker=hp_reco_Recommended%2BItems_2_13.productCard.PMU_V2_Kemei%2Bkm-632%2B%2BRuntime%253A%2B45%2Bmin%2BTrimmer%2Bfor%2BMen_TMRFNH6ZQXPXSG3H_personalisedRecommendation%2Fp2p-same_1&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2Fp2p-same_Recommended%2BItems_DESKTOP_HORIZONTAL_productCard_cc_2_NA_view-all&cid=TMRFNH6ZQXPXSG3H'
resp = requests.get(url).content
#print(resp)
soup = BeautifulSoup(resp, 'html.parser')
a_soup=soup.find_all('div',class_='_3pLy-c')
#print(a_soup.text)
'''title=soup.find_all('div',class_='_4rR01T')
for phone in title:
      print(phone.text)
spc=soup.find('ul',class_='_1xgFaf')
print(spc.text)

# print(neat.prettify())
'''
k=1
for card in a_soup:
      title=card.find('div',class_='_4rR01T')
      print(k,'-',title.text)
      reviws=card.find('span',class_='_2_R_DZ')
      print(reviws.text)
      spec=card.find('ul',class_='_1xgFaf')
      print(spec.text.replace('|','\n'))
      price=card.find('div',class_='_30jeq3')
      print(price.text)
      ex=card.find('div',class_='_13J9qT')
      print(ex.text)
      k+=1
      print('------------------------------------------')
