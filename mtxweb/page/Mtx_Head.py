from time import sleep

from mtxweb.page.Base_Page import Base_Page
from selenium import webdriver

class Mtx_Head(Base_Page):

    def __init__(self):
        super().__init__(dev)


    def add_cookies(self):
        self.dev.get("http://121.42.15.146:9090/mtx/")
        sleep(2)
        self.dev.add_cookie({'name':'PHPSESSID','value':'o37s9ebl10ui1s15hcglfl55h6'})
        sleep(2)
        self.dev.refresh()


    def preson(self):
        self.mtx_find_xpath("//span[text()='个人中心']").click()

    def myshop(self):
        self.mtx_find_xpath("//i/following-sibling::span[text()='我的商城']").click()
        self.mtx_find_xpath("//li/a[text()='我的订单']").click()

    def mycollection(self):
        self.mtx_find_xpath("//i/following-sibling::span[text()='我的收藏']").click()
        self.mtx_find_xpath("//li/a[text()='商品收藏']").click()

    def mycar(self):
        self.mtx_find_xpath("//a/span[text()='购物车']").click()

    def myinfo(self):
        self.mtx_find_xpath("//a/span[text()='消息']").click()

    def out(self):
        self.dev.quit()




if __name__ == '__main__':
    dev = webdriver.Chrome()
    obj = Mtx_Head(dev)
    obj.add_cookies()
    obj.preson()
    obj.myshop()
    obj.mycollection()
    obj.mycar()
    obj.out()

