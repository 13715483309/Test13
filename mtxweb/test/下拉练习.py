from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select

dev = webdriver.Chrome()
dev.get("http://sahitest.com/demo/selectTest.htm")
dev.implicitly_wait(5)

select = dev.find_element_by_id('s1Id')
Select(select).select_by_index(2)

sleep(1)
dev.quit()