from mtxapi.api.Base_Api import Base_Api
import requests

class Mtx_Colletion(Base_Api):

    # def __init__(self):
    #     self.ip = 'http://121.42.15.146:9090'
    #     self.headers = {
    #         'X-Requested-With': 'XMLHttpRequest',
    #     }

    def login(self):
        url = self.ip + '/mtx/index.php?s=/index/user/login.html'
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
        }
        data={
            'accounts': 'li40',
            'pwd': '123456'
        }
        res = requests.post(url=url,headers=headers,data=data)
        return res.cookies

    def colletion(self):
        path = '/mtx/index.php?s=/index/userfavor/goods.html'
        cookies = self.login()
        res = self.mtx_get(path)
        return res

if __name__ == '__main__':
    obj = Mtx_Colletion()
    obj.colletion()