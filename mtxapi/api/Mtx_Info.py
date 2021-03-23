import requests

from mtxapi.api.Base_Api import Base_Api


class Mtx_Info(Base_Api):

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

    def get_info(self):
        path = '/mtx/index.php?s=/index/message/index.html'
        res = self.mtx_get(path)
        return res

if __name__ == '__main__':
    obj = Mtx_Info()
    obj.get_info()