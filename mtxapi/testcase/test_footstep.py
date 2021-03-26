import pytest

from mtxapi.api.Mtx_Footstep import Mtx_Footstep
from mtxapi.api.Mtx_Login import Mtx_Login
from mtxapi.log.Logger import Logger


class Test_Footstep():

    def setup_class(self):
        self.loginobj = Mtx_Login()
        self.loggerinobj = Logger().get_logger()
        self.footobj = Mtx_Footstep()
        self.loggerinobj.info('初始化')

    def test_login(self):
        res = self.loginobj.login('li40','123456')
        pytest.assume(res['msg']=='登录成功')
        self.loggerinobj.info('登录')

    @pytest.mark.parametrize('kw', [('手机','')])
    def test_footstep(self, kw):
        res = self.footobj.footstep_search(kw)
        pytest.assume('我的足迹 - 码同学实战系统' in res)
        self.loggerinobj.info('搜索')

if __name__ == '__main__':
    pytest.main(['-s'])