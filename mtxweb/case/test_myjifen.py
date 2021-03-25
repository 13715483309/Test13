import pytest
from selenium import webdriver

from mtxweb.page.Mtx_Left import Mtx_Left
from mtxweb.page.Mtx_Login import Mtx_Login
from mtxweb.page.Mtx_Myjifen import Mtx_Myjifen
from mtxweb.tools.log import Logger


class Test_Myjifen():

    def setup_class(self):
        self.dev = webdriver.Chrome()
        self.loggerobj = Logger().get_logger()
        self.loginobj = Mtx_Login(self.dev)
        self.leftobj = Mtx_Left(self.dev)
        self.jifenobj = Mtx_Myjifen(self.dev)
        self.loggerobj.info("初始化")

    def test_login(self):
        self.loginobj.login()
        self.loggerobj.info("登录")

    def test_goto_jifen(self):
        self.leftobj.myshopt()
        self.leftobj.myjifen()
        self.loggerobj.info("积分页面")

    def test_search(self):
        self.jifenobj.jifen_search()
        self.loggerobj.info("搜索")

    def test_search_condition(self):
        self.jifenobj.jifen_clear()
        self.jifenobj.jifen_search_condition()
        self.loggerobj.info("搜索条件")

    def teardown_class(self):
        self.dev.quit()
        self.loggerobj.info("退出")

if __name__ == '__main__':
    pytest.main(['-s'])