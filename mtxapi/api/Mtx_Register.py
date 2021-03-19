import requests

from mtxapi.api.Base_Api import Base_Api


class Mtx_Register(Base_Api):

    def register(self,data):
        path = '/mtx/index.php?s=/index/user/reg.html'
        # data = {
        #     'accounts': 'li41',
        #     'pwd': '123456',
        #     'type': 'username',
        #     'is_agree_agreement': 1
        # }
        res = self.mtx_post(path, data)
        return res

if __name__ == '__main__':
    obj = Mtx_Register()
    obj.register()