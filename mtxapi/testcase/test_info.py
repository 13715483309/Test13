import pytest

from mtxapi.api.Mtx_Info import Mtx_Info
from mtxapi.api.Mtx_Login import Mtx_Login
from mtxapi.log.Logger import Logger


class Test_Info():

    def setup_class(self):
        self.loginobj = Mtx_Login()
        self.loggerobj = Logger().get_logger()
        self.infoobj = Mtx_Info()

    @pytest.mark.parametrize('account,pwd',[('li40','123456')])
    def test_login(self,account,pwd):
        res = self.loginobj.login(account,pwd)
        if pytest.assume(res['msg']=='登录成功'):
            self.loggerobj.info('登录断言成功')
        else:
            self.loggerobj.info('登录断言失败')

    def test_info(self):
        res = self.infoobj.get_info()
        if pytest.assume('我的消息 - 码同学实战系统' in res.text):
            self.loggerobj.info('消息模块查询成功')
        else:
            self.loggerobj.info('消息模块查询失败')

if __name__ == '__main__':
    pytest.main(['-s'])
