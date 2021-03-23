from selenium import webdriver

from mtxweb.page.Mtx_Left import Mtx_Left
from mtxweb.page.Mtx_Login import Mtx_Login
from mtxweb.page.Mtx_Safe import Mtx_Safe
from mtxweb.tools.log import Logger
import pytest

class Test_Safe():

    def setup_class(self):
        self.dev = webdriver.Chrome()
        self.loginobj = Mtx_Login(self.dev)
        self.leftobj = Mtx_Left(self.dev)
        self.safeobj = Mtx_Safe(self.dev)
        self.logerobj = Logger().get_logger()
        self.logerobj.info('初始化')

    def test_login(self):
        self.loginobj.login()
        self.logerobj.info('登录')


    def test_goto_safe(self):
        self.leftobj.myshopt()
        self.leftobj.safe()
        self.logerobj.info('跳转到安全设置页面')

    def test_safe(self):
        self.safeobj.name_pwd()
        self.logerobj.info('账号密码修改')

    def teardown_class(self):
        self.dev.quit()

if __name__ == '__main__':
    pytest.main(['-s'])