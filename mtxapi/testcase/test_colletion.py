import pytest

from mtxapi.api.Mtx_Login import Mtx_Login
from mtxapi.api.Mtx_colletion import Mtx_Colletion
from mtxapi.log.Logger import Logger


class Test_Collection():

    def setup_class(self):
        self.colltionobj = Mtx_Colletion()
        self.loggerobj = Logger().get_logger()
        self.loginobj = Mtx_Login()

    @pytest.mark.parametrize('account,pwd',[('li40','123456')])
    def test_case_login(self,account,pwd):
        res = self.loginobj.login(account,pwd)
        pytest.assume(res['msg']=='登录成功')
        self.loggerobj.info('登录操作')

    def test_case_collection(self):
        res = self.colltionobj.colletion()
        # print(res)
        # assert "我的收藏 - 码同学实战系统" in res.text
        pytest.assume('我的收藏 - 码同学实战系统' in res.text)
        self.loggerobj.info('收藏列表页')

if __name__ == '__main__':
    pytest.main(['-s'])