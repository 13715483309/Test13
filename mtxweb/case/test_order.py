import pytest

from mtxweb.page.Mtx_Left import Mtx_Left
from mtxweb.page.Mtx_Login import Mtx_Login
from mtxweb.page.Mtx_Order import Mtx_Order
from mtxweb.tools.log import Logger
from selenium import webdriver

class Test_Order():

    def setup_class(self):
        self.dev = webdriver.Chrome()
        self.loginobj = Mtx_Login(self.dev)
        self.loggerobj = Logger().get_logger()
        self.orderobj = Mtx_Order(self.dev)
        self.leftobj = Mtx_Left(self.dev)

    def test_login(self):
        self.loggerobj.info("登录")
        self.loginobj.login()

    def test_goto_order(self):
        self.loggerobj.info("跳转到订单页面")
        self.leftobj.myshopt()
        self.leftobj.order()

    def test_order(self):
        self.loggerobj.info("订单条件处理")
        self.orderobj.search_condition()

    def teardown_class(self):
        self.dev.quit()

if __name__ == '__main__':
    pytest.main(['-s'])
