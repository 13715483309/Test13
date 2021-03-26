import requests

from mtxapi.api.Base_Api import Base_Api


class Mtx_Footstep(Base_Api):

    def footstep_search(self,kw):
        path = '/mtx/index.php?s=/index/usergoodsbrowse/index.html'
        data = {
            'keywords': kw
        }
        res = self.mtx_post(path,data)
        return res


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


    def footstep_search_no(self):
        url = 'http://121.42.15.146:9090/mtx/index.php?s=/index/usergoodsbrowse/index.html'
        data = {
            'keywords': '手机'
        }
        cookies = self.login()
        res = requests.post(url=url,cookies=cookies,data=data)
        print(res.text)

if __name__ == '__main__':
    obj = Mtx_Footstep()
    obj.footstep_search()
