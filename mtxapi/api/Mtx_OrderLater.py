import requests

from mtxapi.api.Base_Api import Base_Api


class Mtx_OrderLater(Base_Api):

    def login(self):
        url = 'http://121.42.15.146:9090/mtx/index.php?s=/index/user/login.html'
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
        }
        data = {
            'accounts': 'li40',
            'pwd': '123456'
        }
        res = requests.post(url=url, headers=headers, data=data)
        return res.cookies

    def orderlater_no(self):
        cookies = self.login()
        url = "http://121.42.15.146:9090/mtx/index.php?s=/index/orderaftersale/index.html"
        data = {
            'keywords': '124',
            'is_more': 0,
            'type': 0,
            'status': 0,
            'refundment': 1
        }
        res = requests.post(url=url,cookies=cookies,data=data)
        print(res.text)

    def orderlater(self,kw,more,type,status,refundent):
        path = '/mtx/index.php?s=/index/orderaftersale/index.html'
        data = {
            'keywords': kw,
            'is_more': more,
            'type': type,
            'status': status,
            'refundment': refundent
        }
        res = self.mtx_post(path,data)
        return res

    def orderlaters(self, kw, **kwargs):
        path = '/mtx/index.php?s=/index/orderaftersale/index.html'
        data = {
            'keywords': kw,
            **kwargs
        }
        print(data)
        res = self.mtx_post(path, data)
        return res

if __name__ == '__main__':
    obj = Mtx_OrderLater()
    obj.orderlater_no()