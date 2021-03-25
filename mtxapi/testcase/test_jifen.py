import pytest

from mtxapi.api.Mtx_Login import Mtx_Login
from mtxapi.api.Mtx_jifen import Mtx_Jifen
from mtxapi.log.Logger import Logger


class Test_Jifen:

    def setup_class(self):
        self.jifenobj = Mtx_Jifen()
        self.loggerobj = Logger().get_logger()
        self.loginobj = Mtx_Login()
        self.loggerobj.info('初始化')

    @pytest.mark.parametrize('account,pwd',[('li40','123456')])
    def test_login(self,account,pwd):
        res = self.loginobj.login(account,pwd)
        pytest.assume(res['msg']=='登录成功')
        self.loggerobj.info('登录')

    @pytest.mark.parametrize('kw,type',[('手机','-1')])
    def test_jifen(self,kw,type):
        res = self.jifenobj.jifen(kw,type)
        pytest.assume('我的积分 - 码同学实战系统' in res)
        self.loggerobj.info('我的积分')

if __name__ == '__main__':
    pytest.main(['-s'])