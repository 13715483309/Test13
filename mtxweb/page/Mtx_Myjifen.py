from selenium.webdriver.support.select import Select

from mtxweb.page.Base_Page import Base_Page
from selenium import webdriver

from mtxweb.page.Mtx_Left import Mtx_Left
from mtxweb.tools.Add_Cookies import Add_Cookies
import os
import yaml

class Mtx_Myjifen(Base_Page):
    current_path = os.path.abspath(__file__)
    data_path = os.path.join(os.path.dirname(current_path)+os.path.sep+'../data','mtx_myjifen.yml')
    with open(data_path,encoding='utf8') as f:
        data = yaml.safe_load(f)
    keywords = data['keywords']
    search1 = data['search1']
    sear_more = data['sear_more']
    sear_type = data['sear_type']
    search2 = data['search2']
    sear_clear = data['sear_clear']


    def __init__(self,dev):
        super().__init__(dev)

    def add_cookie(self):
        Add_Cookies().adcook(self.dev)

    def goto_jifen(self):
        self.leftobj = Mtx_Left(self.dev)
        self.leftobj.myshopt()
        self.leftobj.myjifen()

    def jifen_search(self):
        self.mtx_find_xpath(self.keywords).send_keys('手机')
        self.mtx_find_xpath(self.search1).click()

    def jifen_search_condition(self):
        more = self.mtx_find_xpath(self.sear_more)
        if more:
            more.click()
        js1 = 'document.getElementsByName("type")[0].style.display="block"'
        self.dev.execute_script(js1)
        sel1 = self.mtx_find_xpath(self.sear_type)
        Select(sel1).select_by_visible_text("增加")
        self.mtx_find_xpath(self.search2).click()

    def jifen_clear(self):
        more = self.mtx_find_xpath(self.sear_more)
        if more:
            more.click()
        self.mtx_find_xpath(self.sear_clear).click()

if __name__ == '__main__':
    dev = webdriver.Chrome()
    obj = Mtx_Myjifen(dev)
    obj.add_cookie()
    obj.goto_jifen()
    obj.jifen_search()
    obj.jifen_clear()
    obj.jifen_search_condition()