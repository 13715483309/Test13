'''
单独提取cookies，然后传递
'''
import requests

class Mtx_Order():

    def __init__(self):
        self.ip = 'http://121.42.15.146:9090'
        self.headers = {'X-Requested-With': 'XMLHttpRequest'}

    def login(self):
        url = self.ip + '/mtx/index.php?s=/index/user/login.html'
        data = {
            'accounts': 'li',
            'pwd': '123456'
        }
        res = requests.post(url=url,headers=self.headers,data=data)
        return res.cookies

    def order(self):
        url = self.ip + '/mtx/index.php?s=/index/buy/add.html'
        cookies = self.login()
        print(cookies)
        data = {
            'goods_id': 5,
            'buy_type': 'goods',
            'stock': 1,
            'spec': '',
            'ids': '',
            'address_id': 1380,
            'payment_id': 2,
            'user_note': '',
            'site_model': 0
        }
        res = requests.post(url=url,headers=self.headers,data=data,cookies=cookies)
        print(res.text)

if __name__ == '__main__':
    obj = Mtx_Order()
    # obj.login()
    obj.order()