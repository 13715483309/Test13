from mtxweb.tools.Add_Cookies import Add_Cookies
from mtxweb.page.Base_Page import Base_Page
from selenium import webdriver

class Mtx_Left(Base_Page):

    def __init__(self,dev):
        super().__init__(dev)

    def add_cookies(self):
        self.cookobj = Add_Cookies()
        self.cookobj.adcook(self.dev)

    # 我的商城
    def myshopt(self):
        self.mtx_find_xpath("//a/b/following-sibling::span[text()='我的商城']").click()

    # 个人中心
    def preson(self):
        self.mtx_find_xpath("//a[contains(text(),'个人中心')]").click()

    #订单管理
    def order(self):
        self.mtx_find_xpath("//a[contains(text(),'订单管理')]").click()

    # 订单售后
    def order_later(self):
        self.mtx_find_xpath("//a[contains(text(),' 订单售后')]").click()

    # 我的收藏
    def colletion(self):
        self.mtx_find_xpath("//a[contains(text(),' 我的收藏')]").click()

    # 我的积分
    def myjifen(self):
        self.mtx_find_xpath("//a[contains(text(),' 我的积分')]").click()

    # 个人资料
    def personaldata(self):
        self.mtx_find_xpath("//a[contains(text(),'个人资料')]").click()

    # 我的地址
    def myaddress(self):
        self.mtx_find_xpath("//a[contains(text(),' 我的地址')]").click()


    # 安全设置
    def safe(self):
        self.mtx_find_xpath("//a[contains(text(),' 安全设置')]").click()

    # 我的消息
    def myinfo(self):
        self.mtx_find_xpath("//a[contains(text(),' 我的消息')]").click()

    # 我的足迹
    def myfoot(self):
        self.mtx_find_xpath("//a[contains(text(),' 我的足迹')]").click()

    # 问答
    def answite(self):
        self.mtx_find_xpath("//a[contains(text(),' 问答')]").click()

    # 安全退出
    def loginout(self):
        self.mtx_find_xpath("//a[contains(text(),'安全退出')]").click()

    def out(self):
        self.dev.quit()

if __name__ == '__main__':
    dev = webdriver.Chrome()
    obj = Mtx_Left(dev)
    obj.add_cookies()
    obj.myshopt()
    obj.preson()
    obj.order()
    obj.order_later()
    obj.colletion()
    obj.myjifen()
    obj.personaldata()
    obj.myaddress()
    obj.safe()
    obj.myinfo()
    obj.myfoot()
    obj.answite()
    obj.loginout()
    obj.out()
