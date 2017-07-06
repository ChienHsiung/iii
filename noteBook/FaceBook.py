import requests
import json

res =requests.get('https://developers.facebook.com/tools/explorer/145634995501895/?method=GET&path=me%3Ffields%3Did%2Cname%2Cbirthday%2Ccontext&version=v2.9')
print(res.status_code)
print(res.json())
