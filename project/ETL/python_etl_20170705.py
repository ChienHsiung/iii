
# coding: utf-8

# #### FB Graph API
# #### HTTP states(Cookies, Sessions)
# ##### Example:
# 1. PTT
# 
# ### Review and Concusion: HTTP and the web
# 
# #### Selenium
# #### Common transformations(Datetime, numbers, strings)
# #### Regular expression

# In[1]:


# FB Graph API
import requests

res = requests.get("https://graph.facebook.com/v2.9/1068531466501015/feed", params={
    "access_token": "EAACEdEose0cBAKsB75S34ME72rTZBQR41YZB2fZCdpdQ7ZAqNBaEtSKRHHeJ6PvIYSO7Esx36Pz3G1WhQ0qW0BtKyXdHST7ZCfC6sGo8TwDVtFcufQjZCkyi49QSnTPyc475tW9eTuC2raZCLDQitHUHDEqQrqbaZC0zYkZAqrLy3FcmyBsJBGZAKGDwokKcDStxMZD",
    "fields": "message,comments.limit(500).sort(reverse_chronological),attachments",
    "limit": 20
})


# In[3]:


res.status_code


# In[10]:


res.json().keys()


# In[11]:


res.json()['paging']


# In[13]:


while True:
    next_url = res.json()['paging']['next']
    print("[INFO] crawling %s"%next_url)
    res = requests.get(next_url)
    print("[INFO] %s finished"%next_url)
    with open('fb_%s.json'%(res.json()['paging']['next'].split('until=')[1].split('&__pag')[0]), 'w') as f:
        f.write(res.text)


# In[14]:


get_ipython().system('ls')


# In[19]:


import json

fb_data = json.load(open('./fb_1498720637.json'))


# In[20]:


type(fb_data)


# # HTTP State management

# In[22]:


# PTT
import requests

URL = "https://www.ptt.cc/bbs/Gossiping"
res = requests.get(URL)
print(res.text)


# In[23]:


res.request.headers


# In[1]:


# PTT
import requests

URL = "https://www.ptt.cc/bbs/Gossiping"
res = requests.get(URL, headers={"cookie": "over18=1;"})
print(res.text)
res.request.headers


# In[2]:


# PTT
import requests

URL = "https://www.ptt.cc/bbs/Gossiping"
res = requests.get(URL, cookies={"over18": "1"})
print(res.text)
res.request.headers


# In[10]:


# PTT
import requests

URL = "https://www.ptt.cc/bbs/Gossiping"
res = requests.get(URL, headers={"cookie": "over18=1"}, allow_redirects=False)
print(res.text)
res.request.headers


# In[29]:


# PTT
import requests

URL = "https://www.ptt.cc/bbs/Gossiping"
res = requests.get(URL, headers={"cookie": "over18=1"})
print(res.text)

# res.history -> list of Response objects created during this request
print("Num of responses: %s"%(len(res.history)))
print(res.history)
res.history[0].request.headers
#res.history[1].request.headers


# In[31]:


import requests

requests.get("https://google.com")
requests.get("https://google.com")


# In[34]:


from requests import Session

rs = Session()
rs.get("https://google.com")
rs.get("https://google.com")


# In[1]:


from requests import Session

def str2dict(data_str):
    data = {}
    for row in data_str.split('\n'):
        kv_list = row.split(":")
        data[kv_list[0]] = kv_list[1]
    return data

form_data = str2dict("""method:search
searchMethod:true
searchTarget:ATM
orgName:
orgId:
hid_1:1
tenderName:
tenderId:
tenderStatus:4,5,21,29
tenderWay:
awardAnnounceStartDate:106/07/02
awardAnnounceEndDate:106/07/03
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


URL = "http://web.pcc.gov.tw/tps/pss/tender.do?searchMode=common&searchType=advance"

rs = Session()
res = rs.post(URL, data=form_data)


# In[36]:


res.status_code


# In[2]:


res.text


# In[38]:


res2 = rs.get("http://web.pcc.gov.tw/tps/pss/tender.do?searchMode=common&searchType=advance&searchTarget=ATM&method=search&isSpdt=&pageIndex=2&execLocationArea=")


# In[39]:


res2.status_code


# In[40]:


res2.text


# # yes123

# In[108]:


URL = "https://www.yes123.com.tw/admin/job_refer_list.asp"

form_data = str2dict("""find_key1:程式設計師
search_work:職務
search_multi_loc:地區
find_key2:
search_multi_loc2:請選擇地區
search_work2:請選擇職務
search_job2:請選擇行業
find_key3:
search_multi_loc3:請選擇地區
search_work3:請選擇職務
search_subj:請選擇你的科系
search_work4:
search_multi_loc4:請選擇地區
search_multi_loc5:請選擇地區
search_work6:
search_work7:
search_multi_loc6:
search_work8:
search_multi_loc7:
search_work9:請選擇職務
find_sf_subj_mode1:
s_find_sf_subj_mode1:
find_se_work_mode1:
s_find_se_work_mode1:
find_ss_work_mode1:
s_find_ss_work_mode1:
find_zone_mode1:
find_zone_mode2:
find_zone_mode3:
find_zone_mode4:
find_zone_mode5:
find_zone_mode6:
find_zone_mode7:
find_zone_mode8:
find_zone_mode9:
find_zone_mode10:
s_find_zone_mode1:
s_find_zone_mode2:
s_find_zone_mode3:
s_find_zone_mode4:
s_find_zone_mode5:
s_find_zone_mode6:
s_find_zone_mode7:
s_find_zone_mode8:
s_find_zone_mode9:
s_find_zone_mode10:
find_metro_mode1:
find_metro_mode2:
find_metro_mode3:
find_metro_mode4:
find_metro_mode5:
find_metro_mode6:
find_metro_mode7:
find_metro_mode8:
find_metro_mode9:
find_metro_mode10:
s_find_metro_mode1:
s_find_metro_mode2:
s_find_metro_mode3:
s_find_metro_mode4:
s_find_metro_mode5:
s_find_metro_mode6:
s_find_metro_mode7:
s_find_metro_mode8:
s_find_metro_mode9:
s_find_metro_mode10:
find_map_mode1:
find_map_mode2:
find_map_mode3:
find_map_mode4:
find_indy_mode1:
find_indy_mode2:
find_indy_mode3:
find_indy_mode4:
find_indy_mode5:
find_indy_mode6:
find_indy_mode7:
find_indy_mode8:
find_indy_mode9:
find_indy_mode10:
s_find_indy_mode1:
s_find_indy_mode2:
s_find_indy_mode3:
s_find_indy_mode4:
s_find_indy_mode5:
s_find_indy_mode6:
s_find_indy_mode7:
s_find_indy_mode8:
s_find_indy_mode9:
s_find_indy_mode10:
find_scl_mode1:
find_scl_mode2:
find_scl_mode3:
find_scl_mode4:
find_scl_mode5:
find_scl_mode6:
find_scl_mode7:
find_scl_mode8:
find_scl_mode9:
find_scl_mode10:
s_find_scl_mode1:
s_find_scl_mode2:
s_find_scl_mode3:
s_find_scl_mode4:
s_find_scl_mode5:
s_find_scl_mode6:
s_find_scl_mode7:
s_find_scl_mode8:
s_find_scl_mode9:
s_find_scl_mode10:
find_work_mode1:
find_work_mode2:
find_work_mode3:
find_work_mode4:
find_work_mode5:
find_work_mode6:
find_work_mode7:
find_work_mode8:
find_work_mode9:
find_work_mode10:
s_find_work_mode1:
s_find_work_mode2:
s_find_work_mode3:
s_find_work_mode4:
s_find_work_mode5:
s_find_work_mode6:
s_find_work_mode7:
s_find_work_mode8:
s_find_work_mode9:
s_find_work_mode10:
find_job_mode1:
find_job_mode2:
find_job_mode3:
find_job_mode4:
find_job_mode5:
find_job_mode6:
find_job_mode7:
find_job_mode8:
find_job_mode9:
find_job_mode10:
s_find_job_mode1:
s_find_job_mode2:
s_find_job_mode3:
s_find_job_mode4:
s_find_job_mode5:
s_find_job_mode6:
s_find_job_mode7:
s_find_job_mode8:
s_find_job_mode9:
s_find_job_mode10:
find_sche_mode1:
find_sche_mode2:
find_sche_mode3:
find_sche_mode4:
find_sche_mode5:
s_find_sche_mode1:
s_find_sche_mode2:
s_find_sche_mode3:
s_find_sche_mode4:
s_find_sche_mode5:
_mu_sf_1:
_mu_se_1:
_mu_chkbox_2:
_mu_chkbox_3:
_mu_wk_1:
_mu_wk_2:
_mu_wk_3:
_mu_wk_4:
_mu_wk_5:
_mu_job_1:
_mu_edu_1:
_mu_edu_2:
_mu_edu_3:
_mu_edu_4:
_mu_edu_5:
_mu_edu_6:
_mu_edu_7:
_mu_year_1:
_mu_year_2:
_mu_lang_1:
_mu_lang_2:
_mu_lang_3:
_mu_psn_1:
_mu_time_1:
_mu_time_2:
_mu_time_3:
_mu_time_4:
_mu_time_5:
_mu_vc_1:
_mu_vc_2:
_mu_vc_3:
_mu_vc_4:
_mu_sc_1:
_mu_sc_2:
find_subj_mode1:
find_subj_mode2:
find_subj_mode3:
s_find_subj_mode1:
s_find_subj_mode2:
s_find_subj_mode3:
find_sw_mode1:
find_sw_mode2:
find_sw_mode3:
find_sw_mode4:
find_sw_mode5:
s_find_sw_mode1:
s_find_sw_mode2:
s_find_sw_mode3:
s_find_sw_mode4:
s_find_sw_mode5:
find_cert_mode1:
find_cert_mode2:
find_cert_mode3:
find_cert_mode4:
find_cert_mode5:
s_find_cert_mode1:
s_find_cert_mode2:
s_find_cert_mode3:
s_find_cert_mode4:
s_find_cert_mode5:
find_us_sf_subj_mode1:
s_find_us_sf_subj_mode1:
find_us_se_work_mode1:
s_find_us_se_work_mode1:
find_us_work_mode1:
find_us_work_mode2:
find_us_work_mode3:
find_us_work_mode4:
find_us_work_mode5:
find_us_work_mode6:
find_us_work_mode7:
find_us_work_mode8:
find_us_work_mode9:
find_us_work_mode10:
s_find_us_work_mode1:
s_find_us_work_mode2:
s_find_us_work_mode3:
s_find_us_work_mode4:
s_find_us_work_mode5:
s_find_us_work_mode6:
s_find_us_work_mode7:
s_find_us_work_mode8:
s_find_us_work_mode9:
s_find_us_work_mode10:
find_us_zone_mode1:
find_us_zone_mode2:
find_us_zone_mode3:
find_us_zone_mode4:
find_us_zone_mode5:
find_us_zone_mode6:
find_us_zone_mode7:
find_us_zone_mode8:
find_us_zone_mode9:
find_us_zone_mode10:
s_find_us_zone_mode1:
s_find_us_zone_mode2:
s_find_us_zone_mode3:
s_find_us_zone_mode4:
s_find_us_zone_mode5:
s_find_us_zone_mode6:
s_find_us_zone_mode7:
s_find_us_zone_mode8:
s_find_us_zone_mode9:
s_find_us_zone_mode10:
find_us_metro_mode1:
find_us_metro_mode2:
find_us_metro_mode3:
find_us_metro_mode4:
find_us_metro_mode5:
find_us_metro_mode6:
find_us_metro_mode7:
find_us_metro_mode8:
find_us_metro_mode9:
find_us_metro_mode10:
s_find_us_metro_mode1:
s_find_us_metro_mode2:
s_find_us_metro_mode3:
s_find_us_metro_mode4:
s_find_us_metro_mode5:
s_find_us_metro_mode6:
s_find_us_metro_mode7:
s_find_us_metro_mode8:
s_find_us_metro_mode9:
s_find_us_metro_mode10:
find_us_indy_mode1:
find_us_indy_mode2:
find_us_indy_mode3:
find_us_indy_mode4:
find_us_indy_mode5:
find_us_indy_mode6:
find_us_indy_mode7:
find_us_indy_mode8:
find_us_indy_mode9:
find_us_indy_mode10:
s_find_us_indy_mode1:
s_find_us_indy_mode2:
s_find_us_indy_mode3:
s_find_us_indy_mode4:
s_find_us_indy_mode5:
s_find_us_indy_mode6:
s_find_us_indy_mode7:
s_find_us_indy_mode8:
s_find_us_indy_mode9:
s_find_us_indy_mode10:
find_us_map_mode1:
find_us_map_mode2:
find_us_map_mode3:
find_us_map_mode4:
strrec:0
search_key_word:程式設計師
search_type:job
us_menu:
search_item:1
search_from:index""")

res = requests.post(URL, data=form_data)


# In[109]:


res.status_code


# In[110]:


res.text


# In[111]:


res.encoding = 'utf8'


# In[112]:


res.text


# In[113]:


from bs4 import BeautifulSoup

soup = BeautifulSoup(res.text, 'lxml')


# In[121]:


dd = {'one': 1}
dd['two']


# In[123]:


dd = {'one': 1}
dd.get('two')


# In[130]:


# Pagination
td_tag = soup.select_one("#top_title").find(lambda x: x.get('align') == 'right')
td_tag


# In[133]:


total_page = int(td_tag.text.split('頁')[0].split('/ ')[1])
total_page


# In[57]:


soup.select('a.jobname')


# In[58]:


soup.select('a.jobname')[0]


# In[59]:


# Beautifulsoup Tag objects, attributes can be queries via dictionary
soup.select('a.jobname')[0]['title']


# In[62]:


titles = [job['title'] for job in soup.select('a.jobname')]
titles


# In[63]:


urls = [job['href'] for job in soup.select('a.jobname')]
urls


# In[69]:


uri = "https://www.yes123.com.tw/admin/"

job_list = []
for title,url in zip(titles, urls):
    job_dict = {}
    job_dict['title']  = title
    job_dict['url'] = uri + url
    job_list.append(job_dict)


# In[70]:


job_list


# In[72]:


# YES123 內容頁
import requests
from bs4 import BeautifulSoup

URL = "https://www.yes123.com.tw/admin/job_refer_comp_job_detail2.asp?p_id=6620098_86519539&job_id=20170410120933_6387899"

res = requests.get(URL)


# In[73]:


res.status_code


# In[74]:


res.text


# In[75]:


soup = BeautifulSoup(res.text, 'lxml')


# In[77]:


soup.select('.comp_detail > ul > li')


# In[88]:


soup.select('.comp_detail > ul > li')[0]


# In[91]:


soup.select('.comp_detail > ul > li')[0].select_one('.rr').text


# In[97]:


soup.select('.comp_detail > ul > li')[0].select_one('.rr').text.replace('\r', '\n')


# In[98]:


print(soup.select('.comp_detail > ul > li')[0].select_one('.rr').text.replace('\r', '\n'))


# In[102]:


for kv in soup.select('.comp_detail > ul > li'):
    title = kv.select_one('.tt')
    value = kv.select_one('.rr')
    
    if title:
        print(title.text)
    if value:
        print(value.text.replace('\r', '\n'))
    print("--" * 50)


# In[ ]:




