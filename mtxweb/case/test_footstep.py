import pytest
from selenium import webdriver

from mtxweb.page.Mtx_Footstep import Mtx_Footstep
from mtxweb.page.Mtx_Left import Mtx_Left
from mtxweb.page.Mtx_Login import Mtx_Login
from mtxweb.tools.log import Logger


class Test_Footstep():

    def setup_class(self):
        self.dev = webdriver.Chrome()
        self.loginobj = Mtx_Login(self.dev)
        self.leftobj = Mtx_Left(self.dev)
        self.logerobj = Logger().get_logger()
        self.footobj = Mtx_Footstep(self.dev)
        self.logerobj.info("初始化")

    def test_login(self):
        self.loginobj.login()
        self.logerobj.info("登录")

    def test_goto_foot(self):
        self.leftobj.myshopt()
        self.leftobj.footstep()
        self.logerobj.info("足迹页面")

    def test_footstep(self):
        self.footobj.footstep()
        self.logerobj.info("足迹搜索")


    def teardown_class(self):
        self.dev.quit()

if __name__ == '__main__':
    pytest.main(['-s'])