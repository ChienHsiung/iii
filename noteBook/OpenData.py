import requests
import json
import time

res = requests.get("http://data.ntpc.gov.tw/od/data/api/28AB4122-60E1-4065-98E5-ABCCB69AACA6?$format=json")
res.encoding = 'utf8'
status = res.status_code
if status == 200:
    res = res.json()

    for data in res:
        print(data['time'],data['car'],data['latitude'][:8],data['longitude'][:8],data['location'])
        print('-'*50)

