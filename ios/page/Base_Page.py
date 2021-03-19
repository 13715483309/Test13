from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base_Page():

    def __init__(self):
        self.caps = {
            'bundleId': 'com.apple.MobileAddressBook',
            'platformName': 'ios',
            'platformVersion': '14.4',
            'deviceName': 'iPhone 8',
            'udid': 'B9CB438D-A921-4A96-9669-2AEF547F29F6',
            'automationName': 'XCUITEST',
            'userNewWDA': 'True'
        }
        self.dev = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=self.caps)
        self.dev.implicitly_wait(10)

    def contacts_find_by_xpath(self,path):
        ele = WebDriverWait(self.dev,10,0.5).until(lambda x:x.find_element_by_xpath(path))
        return ele

    def contacts_find_by_ios_predicate(self,path):
        ele = WebDriverWait(self.dev,10,0.5).until(lambda x:x.find_element_by_ios_predicate(path))
        return ele