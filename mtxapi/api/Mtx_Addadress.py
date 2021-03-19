import requests

from mtxapi.api.Base_Api import Base_Api


class Mtx_Addadress(Base_Api):

    def address(self,data):
        path = '/mtx/index.php?s=/index/useraddress/save.html'
        # data = {
        #     'name': 'li',
        #     'tel': '13712321232',
        #     'address': '冬春18号',
        #     'id': '',
        #     'province':6,
        #     'city': 112,
        #     'county': 1567,
        #     'is_default': 1
        # }
        res = self.mtx_post(path, data)
        return res

if __name__ == '__main__':
    obj = Mtx_Addadress()
    obj.address()