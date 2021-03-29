import pytest

from mtxapi.api.Mtx_Login import Mtx_Login
from mtxapi.api.Mtx_OrderLater import Mtx_OrderLater
from mtxapi.log.Logger import Logger


class Test_OrderLater():

    def setup_class(self):
        self.laterobj = Mtx_OrderLater()
        self.loginobj = Mtx_Login()
        self.loggerobj = Logger().get_logger()
        self.loggerobj.info("初始化")

    @pytest.mark.parametrize('accuont,pwd',[('li40','123456')])
    def test_login(self,accuont,pwd):
       res = self.loginobj.login(accuont,pwd)
       try:
           assert res['msg'] == '登录成功'
           self.loggerobj.info('登录成功')
       except Exception as e:
           self.loggerobj.error(f'错误信息提示：{e}')

    @pytest.mark.parametrize('kw,more,type,status,refundent',[('124',0,0,0,1)])
    def test_orderlater(self,kw,more,type,status,refundent):
        res = self.laterobj.orderlater(kw,more,type,status,refundent)
        try:
            pytest.assume('订单售后 - 码同学实战系统' in res)
            self.loggerobj.info('断言成功')
        except Exception as e:
            self.loggerobj.error(f'断言失败{e}')

    # @pytest.mark.skip()
    def test_case_3(self):
        kw = '123'
        a ={'is_more': 1,'type': 0,'status': 0,'refundment': 1 }
        res = self.laterobj.orderlaters(kw,**a)
        # print(res)
        try:
            assert '订单售后 - 码同学实战系统' in res
            self.loggerobj.info('断言成功')
        except Exception as e:
            self.loggerobj.error(f'断言失败{e}')


if __name__ == '__main__':
    pytest.main(['-s'])

