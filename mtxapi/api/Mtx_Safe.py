import requests

from mtxapi.api.Base_Api import Base_Api


class Mtx_Safe(Base_Api):

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

    def safe(self,my,new,confirm):
        path = '/mtx/index.php?s=/index/safety/loginpwdupdate.html'
        data = {
            "my_pwd": my,
            "new_pwd": new,
            "confirm_new_pwd": confirm
        }
        res = self.mtx_post(path,data)
        return res

    def safe_no(self):
        """
        没有继承
        :return:
        """
        url = "http://121.42.15.146:9090/mtx/index.php?s=/index/safety/loginpwdupdate.html"
        headers = {"X-Requested-With":"XMLHttpRequest"}
        data = {
            "my_pwd": '123456',
            "new_pwd": '123456',
            "confirm_new_pwd": '123456'
        }
        res = requests.post(url=url,headers=headers,cookies=self.login(),data=data)
        print(res)
        print(res.text)



if __name__ == '__main__':
    obj = Mtx_Safe()
    obj.safe_no()