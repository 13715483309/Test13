from time import sleep

from selenium import webdriver
import yaml

from mtxweb.page.Base_Page import Base_Page


class Mtx_Login(Base_Page):
    def __init__(self,dev):
        super().__init__(dev)
    with open('/Users/chenjinfei/project/pythonProject/mtxweb/data/mtx_login.yml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    loginurl = data['loginurl']
    account = data['account']
    pwd = data['pwd']
    lo = data['lo']

    def login(self,account='li',pwd='123456'):
        self.dev.get(self.loginurl)
        # self.dev.find_element_by_xpath(self.account).send_keys('zhang')
        # self.dev.find_element_by_xpath(self.pwd).send_keys('123456')
        # self.dev.find_element_by_xpath(self.lo).click()
        self.mtx_find_xpath(self.account).send_keys(account)
        pwds = self.mtx_find_xpath(self.pwd)
        pwds.send_keys(pwd)
        self.mtx_find_xpath(self.lo).click()
        sleep(3)
        # self.dev.quit()

if __name__ == '__main__':
    dev =webdriver.Chrome()
    obj = Mtx_Login(dev)
    obj.login()