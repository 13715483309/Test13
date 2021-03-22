import requests
import json

class Base_Api():

    session = requests.session()

    def __init__(self):
        self.ip = 'http://121.42.15.146:9090'
        self.headers = {
            'X-Requested-With': 'XMLHttpRequest',
        }

    def mtx_post(self,path,data):
        url = self.ip + path
        res = self.session.post(url=url,headers=self.headers,data=data)
        r_j = json.loads(res.text)
        return r_j

    def mtx_get(self,path):
        url = self.ip + path
        res = self.session.get(url)#返回的数据类型是str
        return res