from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

dev = webdriver.Chrome()
dev.get('https://www.baidu.com/s?ie=UTF-8&wd=%E7%99%BE%E5%BA%A6')
dev.implicitly_wait(5)

set = dev.find_element_by_xpath("//a[@name='tj_settingicon']")

ActionChains(dev).move_to_element(set).perform()

# js = 'document.getElementByXpath("//div[@class=\'bdpfmenu\']").style.display=\'block\''
# dev.execute_script(js)
sleep(2)

dev.find_element_by_xpath("//a[text()='搜索设置']").click()
sleep(1)
dev.find_element_by_xpath("//li[contains(text(),'高级搜索')]").click()

sleep(3)

dev.quit()