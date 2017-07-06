
# coding: utf-8

# In[ ]:


get_ipython().system('pip install lxml')


# ^^^^^^^^^^^^^^^^^
# # 先安裝lxml模組，然後重新啟動kernel

# In[46]:


import json
from collections import Counter # import submodule at top level namesapce
import datetime as dt # import with an alias name
from collections import Counter as Ctr # import submodule at top level namespace with an alias

import jieba
from jieba.analyse import extract_tags


# In[127]:


# primitive types
print(123)
print("hi")
print(True)
print(['apple', 'orage', 'grape']) # list
print(('python', 'ruby')) # tuple
print({1,2,3,1,2}) # set
print({
    "name": "Ian",
    "address": "Taipei"
})


# In[8]:


if True:
    print("Hi if is true")
elif False:
    print("Hi I am flase")
else:
    pass


# In[11]:


# Loops
for lang in ['python', 'ruby', 'javascript']:
    print("I write %s"%(lang)) # "I write {lang}".format(lang=lang)


# In[15]:


# Loops
for lang in ['python', 'ruby', 'javascript']:
    print("I write {lang}, I am a {lang} ninja".format(lang=lang)) # "I write {lang}".format(lang=lang)


# In[17]:


while True:
    print("3D printing is cool")
    break


# In[27]:


# List comprehension
USD_price = []
TWD_price = [100, 88, 33]

for price in TWD_price:
    tmp_price = price * 30
    print(tmp_price)
    USD_price.append(tmp_price)
USD_price


# In[29]:


USD_price = [price * 30 for price in TWD_price]
USD_price


# In[68]:


# higher order functions
list(map(lambda x: x * 30, TWD_price))


# In[33]:


books = ['harry potter', 'doraemon', 'pokemon']
[book.title() for book in books if len(book) > 7]


# In[84]:


# Install dict.txt.big
get_ipython().system('wget https://github.com/fxsjy/jieba/raw/master/extra_dict/dict.txt.big')


# In[37]:


# Jieba
jieba.set_dictionary('./dict.txt.big')


# In[38]:


with open('./cai_speech.txt') as f:
    speech = f.read()


# In[43]:


wd_count = Counter()
for word in jieba.cut(speech):
    print(word)
    if word in wd_count:
        wd_count[word] += 1
    else:
        wd_count[word] = 1


# In[45]:


wd_count.most_common(20)


# In[47]:


extract_tags(speech)


# # Functions

# In[48]:


def add(num1, num2):
    res = num1 + num2
    return res


# In[49]:


add(1,4)


# In[52]:


def add_or_incr(num1, num2=1):
    res = num1 + num2
    return res


# In[55]:


add_or_incr(3)


# In[58]:


add_or_incr(2,5)


# In[60]:


def add_three_nums(num1, num2=1, num3=1):
    res = num1 + num2 + num3
    return res


# In[62]:


add_three_nums(num3=6, num1=9)


# In[118]:


def var_args(*args):
    return args

var_args(1,2,3,4)


# In[119]:


var_args(1,2,3,34,4,5,6,6,4)


# In[122]:


def sum(*args):
    res = 0
    for x in args:
        res = res + x
    return res
        


# In[123]:


sum(1,2,3)


# In[124]:


sum(2,3,4,5,6,7,33)


# In[121]:


def keyword_args(**kwargs):
    print(kwargs['name'])
    return kwargs

keyword_args(name="ian", email="ian@largitdata.com")


# In[65]:


# Scoping
x = 5
print(x)
def set_x(num):
    x = num
    print(x)
set_x(44)


# In[77]:


# Classes
class Human:
    
    # class attr
    wiki_name = "H. sapiens"
    
    def __init__(self, name):
        self.name = name
    
    def say(self, msg):
        print("%s: %s"%(self.name, msg))
    
    @classmethod
    def get_species(cls):
        return cls.wiki_name


# In[78]:


ian = Human("Ian")


# In[79]:


ian.say("Hello word")


# In[76]:


ian.wiki_name


# In[80]:


ian.get_species()


# In[115]:


class Batman(Human):
    def __init__(self, name, superpower):
        super(Batman, self).__init__(name)
        self.superpower = superpower
        
    def say(self, msg):
        print("Bat man is saying..")
        super(Batman, self).say(msg)
    
    def punch():
        print("Boom")


# In[116]:


bruce = Batman("Bruce Wayne", "fly")


# In[152]:


bruce.say("Hi I am batman")


# # HTTP Requests

# In[129]:


get_ipython().system('pip install requests')


# In[130]:


import requests


# In[171]:


res = requests.get("http://www.snowtomamu.jp/winter/en/")


# In[172]:


type(res)


# In[173]:


res.status_code


# In[103]:


res.text[:100]


# In[178]:


with open('tomamu.html', 'w') as f:
    f.write(res.text)


# In[179]:


get_ipython().system('ls')


# In[180]:


# https://docs.python.org/3/tutorial/index.html


# In[2]:


# POST
data_str = """method:search
searchMethod:true
searchTarget:ATM
orgName:
orgId:
hid_1:1
tenderName:
tenderId:
tenderStatus:4,5,21,29
tenderWay:
awardAnnounceStartDate:106/06/29
awardAnnounceEndDate:106/06/29
proctrgCate:
tenderRange:
minBudget:
maxBudget:
item:
hid_2:1
gottenVendorName:
gottenVendorId:
hid_3:1
submitVendorName:
submitVendorId:
location:
execLocationArea:
priorityCate:
isReConstruct:
btnQuery:查詢"""


# In[3]:


def str2dict(data_str):
    data = {}
    for row in data_str.split('\n'):
        kv_list = row.split(":")
        data[kv_list[0]] = kv_list[1]
    return data


# In[4]:


data = str2dict(data_str)


# In[5]:


str2dict("""method:search
searchMethod:true
searchTarget:ATM
orgName:
orgId:
hid_1:1
tenderName:
tenderId:
tenderStatus:4,5,21,29
tenderWay:
awardAnnounceStartDate:106/06/28
awardAnnounceEndDate:106/06/28
proctrgCate:
tenderRange:
minBudget:
maxBudget:
item:
hid_2:1
gottenVendorName:
gottenVendorId:
hid_3:1
submitVendorName:
submitVendorId:
location:
execLocationArea:
priorityCate:
isReConstruct:
btnQuery:查詢""")


# In[16]:


import requests
res = requests.post("http://web.pcc.gov.tw/tps/pss/tender.do?searchMode=common&searchType=advance",
             data=data)


# In[17]:


type(res)


# In[18]:


res


# In[10]:


res.status_code


# In[104]:


res.text[:100]


# In[201]:


# Beautifulsoup4
get_ipython().system('pip install beautifulsoup4')


# In[12]:


from bs4 import BeautifulSoup


# In[203]:


BeautifulSoup


# In[206]:


get_ipython().system('pip install lxml')


# In[13]:


soup = BeautifulSoup(res.text, 'lxml')


# In[14]:


soup


# In[15]:


type(soup)


# In[19]:


soup.select('table')


# In[20]:


soup.select("#print_area")


# In[21]:


# Check length of select()
len(soup.select("#print_area"))


# In[24]:


# For further queries..
# Method 1
soup.select("#print_area > table > tr")


# In[25]:


# list of Tag, 102 of them
len(soup.select("#print_area > table > tr"))


# In[27]:


for tr in soup.select("#print_area > table > tr"):
    print(tr.text.strip())


# In[38]:


for td in soup.select("#print_area > table > tr"):
    for field in td.select('td'):
        print(" ".join(field.text.strip().split()))
    print("=="*50)


# In[85]:


# FB Graph API
import requests

res = requests.get("https://graph.facebook.com/v2.9/1068531466501015/feed", params={
    "access_token": "EAACEdEose0cBAIQZAG4ecbEK1ZAQfKUMbJHUTG6xyFfO9PsJLNY8BZBJmZCWF8ujvAQYP4NOvX1ZBuFtw8ORNtKS4uudECZCoYiSTTuWoprDNRL00ZBZCOq2tZBmiOwbCmqx1MOvHzPg0EqqJ4k52s1aqEEVlQPbi9RWUaogKFnhPYIrB76BVCQMirpZAFEHVf0KsZD",
    "fields": "message,comments,attachments",
    "limit": 500
})


# In[86]:


res


# In[87]:


res.headers


# In[105]:


res.json()


# In[89]:


res.json().keys()


# In[106]:


res.json()['data']


# In[92]:


res.json().keys()


# In[93]:


res.json()['paging']


# In[100]:


tm = res.json()['paging']['previous'].split('since=')[1].split('&')[0]
tm


# In[91]:


len(res.json()['data'])


# In[101]:


with open('./fb_%s.json'%tm, 'w') as f:
    f.write(res.text)


# In[ ]:




