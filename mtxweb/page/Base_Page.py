from selenium import webdriver
from selenium.webdriver.support.select import Select
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

    def mtx_js_display(self,name,tex):
        js1 = 'document.getElementsByName("'+name+'")[0].style.display="block";'
        self.dev.execute_script(js1)
        sel1 = self.mtx_find_xpath(f"//select[@name='{name}']")
        Select(sel1).select_by_visible_text(tex)