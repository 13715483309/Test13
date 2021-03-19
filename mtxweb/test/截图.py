from time import sleep

from selenium import webdriver

dev = webdriver.Chrome()
dev.get('https://www.baidu.com')

dev.implicitly_wait(5)
path = '/Users/chenjinfei/project/pythonProject/mtxweb/test/pic/one.png'

dev.get_screenshot_as_file(path)
sleep(1)
dev.quit()