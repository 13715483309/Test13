import pytest
from selenium import webdriver
from mtxweb.page.Mtx_Login import Mtx_Login
from mtxweb.tools.log import Logger


class Test_Login():

    def setup_class(self):
        dev = webdriver.Chrome()
        self.logobj = Mtx_Login(dev)

    #正向case
    @pytest.mark.parametrize('account,pwd',[('zhang','123456')])
    def test_case1(self,account,pwd):
        self.logobj.login(account,pwd)
        path = f"//div[@class='menu-hd']/em[contains(text(),{account})]"
        # assert self.logobj.mtx_find_xpath(path)
        if pytest.assume(self.logobj.mtx_find_xpath(path)):
            Logger().get_logger().info('success')
        else:
            Logger.get_logger().info('faile')

    def teardown_class(self):
        self.logobj.dev.quit()

if __name__ == '__main__':
    pytest.main(['-s'])