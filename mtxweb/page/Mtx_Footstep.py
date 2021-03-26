from selenium import webdriver

from mtxweb.page.Base_Page import Base_Page
from mtxweb.page.Mtx_Left import Mtx_Left
from mtxweb.tools.Add_Cookies import Add_Cookies
import os
import yaml

class Mtx_Footstep(Base_Page):
    cur_path = os.path.abspath(__file__)
    data_path = os.path.join(os.path.dirname(cur_path)+os.path.sep+'../data','mtx_footstep.yml')

    with open (data_path,encoding='utf8') as f:
        data = yaml.safe_load(f)
    keywords = data['keywords']
    search = data['search']

    def __init__(self,dev):
        super().__init__(dev)

    def add_cookies(self):
        Add_Cookies().adcook(self.dev)

    def goto_foot(self):
        self.leftobj = Mtx_Left(self.dev)
        self.leftobj.myshopt()
        self.leftobj.footstep()

    def footstep(self):
        self.mtx_find_xpath(self.keywords).send_keys('手机')
        self.mtx_find_xpath(self.search).click()

if __name__ == '__main__':
    dev = webdriver.Chrome()
    obj = Mtx_Footstep(dev)
    obj.add_cookies()
    obj.goto_foot()
    obj.footstep()