from time import sleep

from appium import webdriver

class SimpleIOS():
    def __init__(self):
        #self.app = '/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Library/Developer/CoreSimulator/Profiles/Runtimes/iOS.simruntime/Contents/Resources/RuntimeRoot/Applications/Contacts.app'
        self.caps ={
            'bundleId': 'com.apple.MobileAddressBook',
            'platformName': 'ios',
            'platformVersion': '14.4',
            'deviceName': 'iPhone 8',
            'udid': 'B9CB438D-A921-4A96-9669-2AEF547F29F6',
            'automationName': 'XCUITEST',
            'userNewWDA': 'True'
        }
        self.dev = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',desired_capabilities=self.caps)
        self.dev.implicitly_wait(10)

    def addbutton(self):
        add = self.dev.find_element_by_ios_predicate("name == 'Add'")
        add.click()
        sleep(3)
        fir = self.dev.find_element_by_ios_predicate("name == 'First name'")
        fir.send_keys('zhang')
        sleep(2)
        last = self.dev.find_element_by_ios_predicate("name == 'Last name'")
        last.click()
        last.send_keys('san')
        sleep(2)
        com=self.dev.find_element_by_ios_predicate("name == 'Company'")
        com.send_keys('beijinglu')
        ins = self.dev.find_element_by_ios_predicate("name == 'Insert add phone'")
        ins.click()
        sleep(2)
        mobile = self.dev.find_element_by_ios_predicate("name == 'mobile'")
        mobile.send_keys('13045342343')
        sleep(2)
        addemail = self.dev.find_element_by_ios_predicate("name == 'add email'")
        addemail.click()
        inputemail = self.dev.find_element_by_ios_predicate("name == 'home'")
        inputemail.send_keys('7867@qq.com')
        sleep(2)
        self.dev.find_element_by_ios_predicate("name == 'Add'").click()
        sleep(3)
        self.dev.quit()

if __name__ == '__main__':
    obj = SimpleIOS()
    obj.addbutton()