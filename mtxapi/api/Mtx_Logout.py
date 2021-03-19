import requests

class Mtx_Logout():

    def __init__(self):
        self.ip = 'http://121.42.15.146:9090'
        self.headers = {'X-Requested-With': 'XMLHttpRequest'}

    def logout(self):
        path = '/mtx/index.php?s=/index/user/logout.html'
        url = self.ip + path
        cookies = {'PHPSESSION':'npfflf0ft17f27mols1vebsdi7'}
        res = requests.post(url=url,headers=self.headers,cookies=cookies)
        print(res)
        # print(res.text)

if __name__ == '__main__':
    obj = Mtx_Logout()
    obj.logout()