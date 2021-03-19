import pytest
from selenium import webdriver
from mtxweb.page.Mtx_Navtion import Mtx_Navtion
from mtxweb.tools.log import Logger


class Test_Navtion():
    def setup_class(self):
        self.dev = webdriver.Chrome()
        self.navobj = Mtx_Navtion(self.dev)
        Logger().get_logger().info('初始化')

    #登录
    def test_case_1(self):
        self.navobj.add_cookies()
        Logger().get_logger().info('登录')

    def test_case_2(self):
        self.navobj.navtion()
        Logger().get_logger().info('导航栏跑一遍')

    def teardown_class(self):
        self.dev.quit()
        Logger().get_logger().info('清除操作')

if __name__ == '__main__':
    pytest.main(['-s'])

