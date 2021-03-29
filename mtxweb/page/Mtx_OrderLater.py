from selenium import webdriver
from selenium.webdriver.support.select import Select

from mtxweb.page.Base_Page import Base_Page
from mtxweb.page.Mtx_Left import Mtx_Left
from mtxweb.tools.Add_Cookies import Add_Cookies
import yaml
import os

class Mtx_OrderLater(Base_Page):
    cur_path = os.path.abspath(__file__)
    data_path = os.path.join(os.path.dirname(cur_path)+os.path.sep+'../data','mtx_orderlater.yml')
    with open(data_path,encoding='utf8') as f:
        dat = yaml.safe_load(f)
    kw = dat['kw']
    more = dat['more']
    find = dat['find']

    def __init__(self,dev):
        super().__init__(dev)

    def add_cookies(self):
        self.cookiesobj = Add_Cookies()
        self.cookiesobj.adcook(self.dev)

    def goto_orderlater(self):
        self.leftobj = Mtx_Left(self.dev)
        self.leftobj.myshopt()
        self.leftobj.order_later()

    def later_searcher(self):
        self.mtx_find_xpath(self.kw).send_keys('123')
        more = self.mtx_find_xpath(self.more)
        if more:
            more.click()

        lis = [('type','仅退款'),('status','待确认'),('refundment','原路退回')]
        for i in lis:
            self.mtx_js_display(i[0],i[1])
        # js1 = 'document.getElementsByName("type")[0].style.display="block";'
        # self.dev.execute_script(js1)
        # sel1 = self.mtx_find_xpath("//select[@name='type']")
        # Select(sel1).select_by_visible_text("仅退款")

        # js2 = 'document.getElementsByName("status")[0].style.display="block";'
        # self.dev.execute_script(js2)
        # sel2 = self.mtx_find_xpath("//select[@name='status']")
        # Select(sel2).select_by_visible_text("待确认")

        # js3 = 'document.getElementsByName("refundment")[0].style.display="block";'
        # self.dev.execute_script(js3)
        # sel3 = self.mtx_find_xpath("//select[@name='refundment']")
        # Select(sel3).select_by_visible_text('原路退回')

        self.mtx_find_xpath(self.find).click()

if __name__ == '__main__':
    dev = webdriver.Chrome()
    obj = Mtx_OrderLater(dev)
    obj.add_cookies()
    obj.goto_orderlater()
    obj.later_searcher()