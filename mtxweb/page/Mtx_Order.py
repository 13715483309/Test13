from selenium.webdriver.support.select import Select

from mtxweb.page.Base_Page import Base_Page
from selenium import webdriver

from mtxweb.page.Mtx_Left import Mtx_Left
from mtxweb.tools.Add_Cookies import Add_Cookies


class Mtx_Order(Base_Page):

    def __init__(self,dev):
        super().__init__(dev)

    def goto_order(self):
        Add_Cookies().adcook(self.dev)
        self.leftobj = Mtx_Left(self.dev)
        self.leftobj.myshopt()
        self.leftobj.order()

    def order_search(self):
        self.mtx_find_xpath("//input[@placeholder='订单号']").clear()
        self.mtx_find_xpath("//input[@placeholder='订单号']").send_keys('234567')
        self.mtx_find_xpath("//button[text()='搜索' and @class='am-btn am-btn-default am-radius']").click()

    def search_condition(self):
        self.mtx_find_xpath("//label[contains(text(),'更多筛选条件')]").click()
        # self.mtx_find_xpath("//a[text()='清除条件']").click()
        self.mtx_find_xpath("//input[@placeholder='起始时间']").click()
        self.mtx_find_xpath("//input[@placeholder='起始时间']").send_keys('2021-03-10')
        ifr3 = self.mtx_find_xpath("//div[@id='edui_fixedlayer']/following::div/iframe")
        self.dev.switch_to.frame(ifr3)
        self.mtx_find_xpath("//input[@id='dpOkInput']").click()
        self.dev.switch_to.default_content()
        self.mtx_find_xpath("//input[@placeholder='结束时间']").click()
        self.mtx_find_xpath("//input[@placeholder='结束时间']").send_keys('2021-03-24')
        ifr3 = self.mtx_find_xpath("//div[@id='edui_fixedlayer']/following::div/iframe")
        self.dev.switch_to.frame(ifr3)
        self.mtx_find_xpath("//input[@id='dpOkInput']").click()
        self.dev.switch_to.default_content()
        self.mtx_find_xpath("//input[@placeholder='最小价格']").send_keys('10')
        self.mtx_find_xpath("//input[@placeholder='最大价格']").send_keys('100')

        self.mtx_find_xpath("//div/a/span[contains(text(),'支付方式')]").click()
        js1 = 'document.getElementsByName("payment_id")[0].style.display=\'block\';'
        self.dev.execute_script(js1)
        sel1 = self.mtx_find_xpath("//select[@name='payment_id']")
        Select(sel1).select_by_visible_text('现金支付')

        self.mtx_find_xpath("//div/a/span[text()='付款状态...']").click()
        js2 = 'document.getElementsByName("pay_status")[0].style.display="block";'
        self.dev.execute_script(js2)
        sel2 = self.mtx_find_xpath("//select[@name='pay_status']")
        Select(sel2).select_by_value('1')

        self.mtx_find_xpath("//div/a/span[text()='订单状态...']").click()
        js3 = 'document.getElementsByName("status")[0].style.display="block";'
        self.dev.execute_script(js3)
        sel3 = self.mtx_find_xpath("//select[@name='status']")
        Select(sel3).first_selected_option

        self.mtx_find_xpath("//div/a/span[text()='评论状态...']").click()
        js4 = 'document.getElementsByName("is_comments")[0].style.display="block";'
        self.dev.execute_script(js4)
        sel4 = self.mtx_find_xpath("//select[@name='is_comments']")
        Select(sel4).select_by_index(1)

        self.mtx_find_xpath("//td/button[text()='搜索']").click()


if __name__ == '__main__':
    dev = webdriver.Chrome()
    obj = Mtx_Order(dev)
    obj.goto_order()
    obj.order_search()
    obj.search_condition()