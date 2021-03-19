from time import sleep

from selenium import webdriver

dev = webdriver.Chrome()
dev.get('http://sahitest.com/demo/formTest.htm')
dev.implicitly_wait(5)
sleep(2)
dev.switch_to.alert.accept()
sleep(2)
dev.quit()