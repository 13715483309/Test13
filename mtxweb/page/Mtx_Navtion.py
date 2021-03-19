from time import sleep

from selenium.webdriver import ActionChains

from mtxweb.page.Base_Page import Base_Page
from mtxweb.tools.Add_Cookies import Add_Cookies
from selenium import webdriver


class Mtx_Navtion(Base_Page):

    def __init__(self,dev):
        super().__init__(dev)

    def add_cookies(self):
        Add_Cookies().adcook(self.dev)

    def navtion(self):
        elements = self.mtx_find_cssSelects(".ml-22")
        lis = ['合约机','雪纺衫','糖果巧克力','洁面乳','婚庆服务','运动器械','机油','遥控车','新生儿','浪漫婚纱']
        j = 0
        for i in range(len(elements)):
            elements = self.mtx_find_cssSelects(".ml-22")
            ActionChains(self.dev).move_to_element(elements[i]).perform()
            sleep(0.5)
            self.mtx_find_xpath(f"//a/span[text()='{lis[j]}']").click()
            j += 1
            sleep(0.5)
            self.dev.back()


if __name__ == '__main__':
    dev = webdriver.Chrome()
    obj = Mtx_Navtion(dev)
    obj.add_cookies()
    obj.navtion()