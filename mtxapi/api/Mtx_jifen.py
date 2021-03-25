import requests

from mtxapi.api.Base_Api import Base_Api


class Mtx_Jifen(Base_Api):

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
        print(res.cookies)
        return res.cookies

    def jifen(self,keywords,type):
        path = '/mtx/index.php?s=/index/userintegral/index.html'
        data = {
            'keywords': keywords,
            'type': type
        }
        res = self.mtx_post(path,data)
        return res

    def jifen_no(self):
        paht = "http://121.42.15.146:9090/mtx/index.php?s=/index/userintegral/index.html"
        cookies = self.login()
        data = {
            'keywords': '123',
            'type': -1
        }
        res = requests.post(url=paht,cookies=cookies,data=data)
        print(res.text)

if __name__ == '__main__':
    obj = Mtx_Jifen()
    obj.jifen()