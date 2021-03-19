import requests

class Mtx_Addaress_Test():

    def __init__(self):
        self.ip = 'http://121.42.15.146:9090'

    def login(self):
        url = self.ip + '/mtx/index.php?s=/index/user/login.html'
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
        }
        data={
            'accounts': 'li',
            'pwd': '123456'
        }
        res = requests.post(url=url,headers=headers,data=data)
        return res.cookies

    def addadr(self):
        url =self.ip + '/mtx/index.php?s=/index/useraddress/save.html'
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
        }
        cookies = self.login()
        data = {
            'name': 'li',
            'tel': '13712321232',
            'address': '冬春18号',
            'alias': 'lili',
            'id': '',
            'province':6,
            'city': 112,
            'county': 1567,
            'is_default': 1
        }
        res = requests.post(url=url,headers=headers,data=data,cookies=cookies)
        print(res.text)



if __name__ == '__main__':
    obj = Mtx_Addaress_Test()
    obj.login()
    obj.addadr()