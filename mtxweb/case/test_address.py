import pytest
from selenium import webdriver
from mtxweb.page.Mtx_Address import Mtx_Address

class Test_Address():

    def setup_class(self):
        dev = webdriver.Chrome()
        self.adrobj = Mtx_Address(dev)

    def test_case_1(self):
        name = self.adrobj.address()
        eles = self.adrobj.dev.find_elements_by_xpath("//span[@class='user']")
        lst = []
        for i in eles:
            lst.append(i.text)
        # print(lst)
        # assert name in lst

    def teardown_class(self):
        self.adrobj.dev.quit()

if __name__ == '__main__':
    pytest.main(['-s'])