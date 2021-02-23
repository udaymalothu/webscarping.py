import mechanize
from bs4 import BeautifulSoup

import pandas as pd

mc = mechanize.Browser()
mc.open('https://www.findandtrace.com/trace-mobile-number-location')

mc.select_form('trace')
mc['mobilenumber'] = '9951918516'
sub = mc.submit()

sub_1 = sub.read()
# print(sub_1)

soup = BeautifulSoup(sub_1, 'html.parser')


tabe_1=[]
tabe=_2=[]

hedad = soup.find('h1')
print(hedad.text)
table = soup.find_all('tfoot')
k = 1
for tables in table:

    print(k, tables.text)

    k += 1

    if k == 3:
        break

h_2 = soup.find('h2')

print(h_2.text)
tables = soup.find('tfoot[1]')
print(tables)
