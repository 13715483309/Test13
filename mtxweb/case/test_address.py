import pytest
from selenium import webdriver
from mtxweb.page.Mtx_Address import Mtx_Address
from mtxweb.page.Mtx_Left import Mtx_Left
from mtxweb.page.Mtx_Login import Mtx_Login


class Test_Address():

    def setup_class(self):
        self.dev = webdriver.Chrome()
        self.adrobj = Mtx_Address(self.dev)
        self.loginobj = Mtx_Login(self.dev)
        self.leftobj = Mtx_Left(self.dev)

    def test_login(self):
        self.loginobj.login()

    def test_goto_address(self):
        self.leftobj.myshopt()
        self.leftobj.myaddress()

    def test_case_1(self):
        # name = self.adrobj.address()
        # eles = self.adrobj.dev.find_elements_by_xpath("//span[@class='user']")
        # lst = []
        # for i in eles:
        #     lst.append(i.text)
        # print(lst)
        # assert name in lst
        self.adrobj.address()

    def teardown_class(self):
        self.adrobj.dev.quit()

if __name__ == '__main__':
    pytest.main(['-s'])