from time import sleep
import yaml
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select

from mtxweb.page.Base_Page import Base_Page


class Mtx_Address(Base_Page):
    current_path = os.path.abspath(__file__)
    data_path = os.path.join(os.path.abspath(os.path.dirname(current_path)+os.path.sep+'../data'),'mtx_address.yml')
    with open(data_path, encoding='utf8') as f:
        data = yaml.safe_load(f)
    preson = data['preson']
    myaddre = data['myaddre']
    adr = data['adr']
    input_name = data['input_name']
    input_tel =data['input_tel']

    def __init__(self,dev):
        super().__init__(dev)

    def address(self):
        self.dev.get("http://121.42.15.146:9090/mtx/")
        sleep(2)
        self.dev.add_cookie({'name':'PHPSESSID','value':'o37s9ebl10ui1s15hcglfl55h6'})
        sleep(2)
        self.dev.refresh()
        self.dev.implicitly_wait(10)
        self.mtx_find_xpath(self.preson).click()
        self.mtx_find_xpath(self.myaddre).click()
        self.mtx_find_xpath(self.adr).click()
        self.dev.switch_to.frame(2)
        self.mtx_find_xpath(self.input_name).send_keys('zhangzhang')
        self.mtx_find_xpath(self.input_tel).send_keys('13713212321')
        # js定位
        js = 'document.getElementsByName("province")[0].style.display="block";'
        self.dev.execute_script(js)
        sel = self.mtx_find_xpath("//select[@name='province']")
        Select(sel).select_by_visible_text('内蒙古自治区')
        js2 = 'document.getElementsByName("city")[0].style.display="block";'
        self.dev.execute_script(js2)
        sel2=self.mtx_find_xpath("//select[@name='city']")
        Select(sel2).select_by_visible_text('包头市')
        js3 = 'document.getElementsByName("county")[0].style.display="block";'
        self.dev.execute_script(js3)
        sel3 = self.mtx_find_xpath("//select[@name='county']")
        Select(sel3).select_by_visible_text("九原区")
        self.mtx_find_xpath("//input[@name='address']").send_keys('测试用的数据')
        self.mtx_find_xpath("//input[@name='alias']").send_keys('zhangzhang')
        self.mtx_find_xpath("//span[text()='否']").click()
        sleep(2)
        self.mtx_find_xpath("//button[text()='保存']").click()
        sleep(3)
        name = 'zhang'
        return name
        # self.dev.quit()

if __name__ == '__main__':
    dev = webdriver.Chrome()
    obj = Mtx_Address(dev)
    obj.address()

