import pytest

from mtxapi.api.Mtx_Login import Mtx_Login
from mtxapi.api.Mtx_buy import Mtx_Buy


class Test_Buy():

    def setup_class(self):
        self.logobj = Mtx_Login()
        self.buyobj = Mtx_Buy()

    #登录操作
    @pytest.mark.parametrize('account,pwd',[('li','123456')])
    def test_case1(self,account,pwd):
        self.logobj.login(account,pwd)

    # 正向case
    @pytest.mark.parametrize(
        'goods_id,buy_type,stock,spec,ids,address_id,payment_id,user_note,site_model',\
            [(5,'goods',1,'','',1380,2,'',0)]
                             )
    def test_case2(self,goods_id,buy_type,stock,spec,ids,address_id,payment_id,user_note,site_model):
        data = {
            'goods_id': goods_id,
            'buy_type': buy_type,
            'stock': stock,
            'spec': spec,
            'ids': ids,
            'address_id': address_id,
            'payment_id': payment_id,
            'user_note': user_note,
            'site_model': site_model
        }
        res = self.buyobj.buy(data)
        pytest.assume(res['msg'] == '提交成功')

    # goods为空
    @pytest.mark.parametrize(
        'goods_id,buy_type,stock,spec,ids,address_id,payment_id,user_note,site_model', \
            [('', 'goods', 1, '', '', 1380, 2, '', 0)]
    )
    def test_case3(self, goods_id, buy_type, stock, spec, ids, address_id, payment_id, user_note, site_model):
        data = {
            'goods_id': goods_id,
            'buy_type': buy_type,
            'stock': stock,
            'spec': spec,
            'ids': ids,
            'address_id': address_id,
            'payment_id': payment_id,
            'user_note': user_note,
            'site_model': site_model
        }
        res = self.buyobj.buy(data)
        print(res)
        pytest.assume(res['msg'] == '商品id有误')

if __name__ == '__main__':
    pytest.main(['-s'])