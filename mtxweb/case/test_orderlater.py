import pytest
from selenium import webdriver

from mtxweb.page.Mtx_Left import Mtx_Left
from mtxweb.page.Mtx_Login import Mtx_Login
from mtxweb.page.Mtx_OrderLater import Mtx_OrderLater
from mtxweb.tools.log import Logger


class Test_Orderlater():

    def setup_class(self):
        self.dev = webdriver.Chrome()
        self.loginobj = Mtx_Login(self.dev)
        self.leftobj = Mtx_Left(self.dev)
        self.ordobj = Mtx_OrderLater(self.dev)
        self.loggerobj = Logger().get_logger()
        self.loggerobj.info('初始化')

    def test_login(self):
        try:
            self.loginobj.login()
            self.loggerobj.info("登录成功")
        except Exception as e:
            self.loggerobj.error(f"异常模块提示{e}")

    def test_goto_orderlate(self):
        try:
            self.leftobj.myshopt()
            self.leftobj.order_later()
            self.loggerobj.info("页面跳转")
        except Exception as e:
            self.loggerobj.error(f'错误信息提示{e}')

    def test_orderlate(self):
        try:
            self.ordobj.later_searcher()
            self.loggerobj.info("售后模块正常")
        except Exception as e:
            self.loggerobj.error(f'异常处理{e}')


    def teardown_class(self):
        self.dev.quit()

if __name__ == '__main__':
    pytest.main(['-s'])