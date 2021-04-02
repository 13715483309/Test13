from selenium import webdriver
from selenium.webdriver.support.select import Select

from mtxweb.page.Base_Page import Base_Page
from mtxweb.page.Mtx_Left import Mtx_Left
from mtxweb.tools.Add_Cookies import Add_Cookies


class Mtx_Info(Base_Page):

    def __init__(self,dev):
        super().__init__(dev)

    def add_cookies(self):
        Add_Cookies().adcook(self.dev)

    def goto_info(self):
        self.leftobj = Mtx_Left(self.dev)
        self.leftobj.myshopt()
        self.leftobj.myinfo()

    def search_no(self):
        self.mtx_find_xpath("//input[@name='keywords']").send_keys('123')
        more = self.mtx_find_xpath("//label/i[@class='am-icon-angle-down']")
        if more:
            more.click()
        lis = [('type','0'),('business_type','3'),('is_read','1')]
        for i in lis:
            self.search_js(i[0],i[1])
        self.mtx_find_xpath("//td/button[text()='搜索']").click()

    def search_js(self,name,value):
        js1 = 'document.getElementsByName("'+name+'")[0].style.display="block";'
        self.dev.execute_script(js1)
        sel1 = self.mtx_find_xpath("//select[@name='"+name+"']")
        Select(sel1).select_by_value(value)

    def search(self):
        pass

if __name__ == '__main__':
    dev = webdriver.Chrome()
    obj = Mtx_Info(dev)
    obj.add_cookies()
    obj.goto_info()
    obj.search_no()