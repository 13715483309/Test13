from time import sleep

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

dev = webdriver.Chrome()
dev.get('http://sahitest.com/demo/')
dev.implicitly_wait(10)
WebDriverWait(dev,10,0.5).until(lambda x:x.find_element_by_xpath("//a[text()='Open Self']")).click()
perhandle = dev.current_window_handle
print(perhandle)
allhandle = dev.window_handles
print(allhandle)
dev.switch_to.window(allhandle[-1])
WebDriverWait(dev,10,0.5).until(lambda x:x.find_element_by_xpath("//a[text()='Alert Test']")).click()
# dev.close()
dev.back()
dev.switch_to.window(perhandle)

WebDriverWait(dev,10,0.5).until(lambda x:x.find_element_by_xpath("//a[text()='Alert Test']")).click()