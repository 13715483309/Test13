import requests

from mtxapi.api.Base_Api import Base_Api


class Mtx_Buy(Base_Api):

    def buy(self,data):
        path = '/mtx/index.php?s=/index/buy/add.html'
        # data = {
        #     'goods_id': 5,
        #     'buy_type': 'goods',
        #     'stock': 1,
        #     'spec': '',
        #     'ids': '',
        #     'address_id': 1380,
        #     'payment_id': 2,
        #     'user_note': '',
        #     'site_model': 0
        # }
        res = self.mtx_post(path,data)
        return res

if __name__ == '__main__':
    obj = Mtx_Buy()
    obj.login()
    obj.buy()
