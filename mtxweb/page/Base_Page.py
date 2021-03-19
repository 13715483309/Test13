from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base_Page():
    # dev = None

    def __init__(self,dev):
        self.dev = dev

    # @classmethod
    # def get_dev(cls):
    #     if cls.dev is None:
    #         cls.dev = webdriver.Chrome()
    #     return cls.dev

    def mtx_find_xpath(self,path):
        ele = WebDriverWait(self.dev,10,0.5).until(lambda x:x.find_element_by_xpath(path))
        return ele

    def mtx_find_cssSelects(self,cs):
        eles = WebDriverWait(self.dev,10,0.5).until(lambda x:x.find_elements_by_css_selector(cs))
        return eles