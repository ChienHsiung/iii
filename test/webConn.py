# -*- coding:utf8 -*-
import requests

URL = "https://www.ptt.cc/bbs/Gossiping"
res = requests.get(URL)
# res = requests.get(URL, cookies={"over18": "1"},allow_redirects=False)
def show(s1):
    print(s1)
    print('-'*50)

show(res.history)
show(res.request.headers)
show(res.headers)
show(res.cookies.values)
show(res.apparent_encoding)
# show(res.text)
# show(res.content)