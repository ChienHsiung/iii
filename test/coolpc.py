# coding: utf-8

import re
import requests
from bs4 import BeautifulSoup as bs
res = requests.get('http://coolpc.com.tw/evaluate.php')
soup = bs(res.text,'lxml')
# data = soup.select('#Tfix')
data = soup.select_one('#Tfix').select('option')
c= 0
for xx in data:
	tmp = str(xx).split('>')[1].replace('</option','').strip()
	if len(tmp) > 3:
		c+=1
		print(tmp)
print('Total: ',c)

