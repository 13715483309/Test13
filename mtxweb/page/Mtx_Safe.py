from mtxweb.page.Base_Page import Base_Page
from selenium import webdriver

from mtxweb.page.Mtx_Left import Mtx_Left
from mtxweb.tools.Add_Cookies import Add_Cookies
import yaml
import os

class Mtx_Safe(Base_Page):
    cur_path = os.path.abspath(__file__)
    data_path = os.path.join(os.path.dirname(cur_path)+os.path.sep+'../data','mtx_safe.yml')
    with open(data_path) as f:
        data = yaml.safe_load(f)

    edit = data['edit']
    my_pwd = data['my_pwd']
    new_pwd = data['new_pwd']
    comfire = data['comfire_pwd']
    safe = data['safe']

    def __init__(self,dev):
        super().__init__(dev)

    def add_cookies(self):
        Add_Cookies().adcook(self.dev)

    def go_to_safe(self):
        self.left = Mtx_Left(self.dev)
        self.left.myshopt()
        self.left.safe()

    def name_pwd(self):
        self.mtx_find_xpath(self.edit).click()
        self.mtx_find_xpath(self.my_pwd).send_keys('123456')
        self.mtx_find_xpath(self.new_pwd).send_keys('123456')
        self.mtx_find_xpath(self.comfire).send_keys('123456')
        self.mtx_find_xpath(self.safe).click()

if __name__ == '__main__':
    dev = webdriver.Chrome()
    obj = Mtx_Safe(dev)
    obj.add_cookies()
    obj.go_to_safe()
    obj.name_pwd()
    dev.quit()
