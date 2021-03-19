import yaml

from mtxapi.api.Base_Api import Base_Api
import os

class Mtx_Login(Base_Api):
    # fpath = os.path()+'../data/mtx_login.yml'
    # fpath = os.path.abspath(os.path.dirname(os.getcwd())) + '/data/mtx_login.yml'
    with open('/Users/chenjinfei/project/pythonProject/mtxapi/data/mtx_login.yml') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)

    def login(self,accounts,pwd):
        path = '/mtx/index.php?s=/index/user/login.html'
        data = {
            'accounts': accounts,
            'pwd': pwd
        }
        res = self.mtx_post(path,data)
        return res

if __name__ == '__main__':
    obj = Mtx_Login()
    obj.login()
