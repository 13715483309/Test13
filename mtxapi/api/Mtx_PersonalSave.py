from mtxapi.api.Base_Api import Base_Api


class Mtx_PersonalSave(Base_Api):

    def login(self):
        path = '/mtx/index.php?s=/index/user/login.html'
        data = {
            'accounts': 'li40',
            'pwd': '123456'
        }
        res = self.mtx_post(path,data)
        print(res)

    def persave(self,data):
        path = '/mtx/index.php?s=/index/personal/save.html'
        # data = {
        #     'nickname': 'li401',
        #     'gender': 2,
        #     'birthday': '2020-09-12'
        # }
        res = self.mtx_post(path, data)
        return res

if __name__ == '__main__':
    obj = Mtx_PersonalSave()
    obj.login()
    obj.persave()