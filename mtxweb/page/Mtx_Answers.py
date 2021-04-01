from selenium import webdriver
from selenium.webdriver.support.select import Select

from mtxweb.page.Base_Page import Base_Page
from mtxweb.page.Mtx_Left import Mtx_Left
from mtxweb.tools.Add_Cookies import Add_Cookies
import yaml
import os

class Mtx_Answers(Base_Page):
    cur_path = os.path.abspath(__file__)
    dpath = os.path.join(os.path.dirname(cur_path)+os.path.sep+'../data','mtx_answers.yml')
    with open(dpath, encoding='utf8') as f:
        data = yaml.safe_load(f)
    keyword = data['keyword']
    more = data['more']
    search = data['search']

    def __init__(self, dev):
        super().__init__(dev)

    def add_cookies(self):
        Add_Cookies().adcook(self.dev)

    def goto_ansers(self):
        self.leftobj = Mtx_Left(self.dev)
        self.leftobj.myshopt()
        self.leftobj.answers()

    def answers(self):
        self.mtx_find_xpath(self.keyword).send_keys('123')
        more = self.mtx_find_xpath(self.more)
        if more:
            more.click()
        lis = [('is_show', '1',0), ('is_reply', '1',0)]
        for i in lis:
            self.answersjs(i[0],i[1],i[2])
        self.mtx_find_xpath(self.search).click()

    def answersjs(self,name,value,type=0):
        js1 = 'document.getElementsByName("'+name+'")[0].style.display="block";'
        self.dev.execute_script(js1)
        sel1 = self.mtx_find_xpath("//select[@name='is_show']")
        if type == 1:
            Select(sel1).select_by_visible_text(f'{value}')
        elif type == 2:
            Select(sel1).select_by_index(value)
        else:
            Select(sel1).select_by_value(value)

if __name__ == '__main__':
    dev = webdriver.Chrome()
    obj = Mtx_Answers(dev)
    obj.add_cookies()
    obj.goto_ansers()
    obj.answers()
