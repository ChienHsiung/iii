# -*- coding:utf8 -*-

# at cmd type chcp 65001

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
# print(res.text.encode(encoding='utf8',errors='strict').decode("cp950", "ignore")) #改變編碼
print(res.text)