from time import sleep
import yaml
from mtxweb.page.Base_Page import Base_Page
from mtxweb.page.Mtx_Left import Mtx_Left
from selenium import webdriver

class Mtx_Personal_Data(Base_Page):
    with open('../data/mtx_personal_data.yml',encoding='utf-8') as f:
        data = yaml.safe_load(f)
    ele_edit = data['edit']
    ele_nickname = data['nickname']
    ele_sex = data['sex']
    ele_birthday = data['birthday']
    ele_iframe3 = data['iframe3']
    ele_makesure = data['makesure']
    ele_save = data['save']

    def __init__(self,dev):
        super().__init__(dev)

    def pre_action(self):
        self.leftobj = Mtx_Left(self.dev)
        self.leftobj.add_cookies()
        self.leftobj.myshopt()
        self.leftobj.personaldata()

    def data_edit(self):
        self.mtx_find_xpath(self.ele_edit).click()
        self.mtx_find_xpath(self.ele_nickname).send_keys("li40")
        self.mtx_find_xpath(self.ele_sex).click()
        birthday = self.mtx_find_xpath(self.ele_birthday)
        birthday.click()
        birthday.send_keys('2001-10-10')
        iframe3 = self.mtx_find_xpath(self.ele_iframe3)
        dev.switch_to.frame(iframe3)
        self.mtx_find_xpath(self.ele_makesure).click()
        dev.switch_to.default_content()
        self.mtx_find_xpath(self.ele_save).click()
        sleep(3)

    def data_personal(self):
        pass

    def out(self):
        self.dev.quit()

if __name__ == '__main__':
    dev = webdriver.Chrome()
    obj = Mtx_Personal_Data(dev)
    obj.pre_action()
    obj.data_edit()
    obj.out()