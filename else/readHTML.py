from bs4 import BeautifulSoup
import requests
res = requests.post("http://web.pcc.gov.tw/tps/pss/tender.do?searchMode=common&searchType=advance",data=data)


def str2dict(data_str):
    data = {}
    for row in data_str.split('\n'):
        kv_list = row.split(":")
        data[kv_list[0]] = kv_list[1]
    return data
