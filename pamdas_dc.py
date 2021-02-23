import requests
from bs4 import BeautifulSoup

url = 'https://www.timeanddate.com/weather/india/Khammam'
resp = requests.get(url).content

soup = BeautifulSoup(resp, 'html.parser')
location_name = soup.find('h1', class_='headline-banner__title')

print(location_name.text)
# print(soup)

main_table = soup.find_all('section', class_='bk-focus')

p_tag = soup.find_all('p')
R_p = p_tag[1].text.replace('F', '\nF')

R_R = R_F = R_p


# print(main_table.text)
def wether():
    for main_tables in main_table:
        cur_temp = main_tables.find('div', class_='h1')
        cur_temps = main_tables.find('div', class_='h2')
        cur_clouds = main_tables.find('p')

        print(cur_temp.text, '\ncurrent temperature is :', cur_temps.text)
        print(cur_clouds.text)
        print(R_R)
        print('----------------------------------------------------')


wether()
sub_tables = soup.find_all('div', class_='bk-focus__info')

sub_table = soup.find_all('tr')
k = 1
for subn in sub_table:
    print(k, subn.text)
    k += 1
    if k == 8:
        break
up_cmg = soup.find_all('table', id='wt-5hr')
for cmg in up_cmg:
    cmg_time = cmg.find('tr', class_='h2')
    print('up coming 5Hr weather like')
    print(cmg_time.text.replace('.', '\t'))
    up_cmptmp = cmg.find('tr', class_='h2 soft')

    print(up_cmptmp.text.replace('C', 'C\t'))
