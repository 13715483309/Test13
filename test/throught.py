# 透传

# 参数透传
import requests
from flask import make_response,json
# import sys
# sys.path.append('/Users/chenjinfei/project/pythonProject/test')
url_t = 'http://127.0.0.1:5000/'

def passThought(url,data):
    url = url_t + url
    res = requests.post(url=url,json=data)
    resp = make_response(res.json())
    return resp