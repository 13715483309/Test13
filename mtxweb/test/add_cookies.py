from time import sleep

from selenium import webdriver

dev = webdriver.Chrome()
dev.get('http://121.42.15.146:9090/mtx/')
sleep(2)
dev.add_cookie({'name':'PHPSESSID','value':'o37s9ebl10ui1s15hcglfl55h6'})
sleep(5)
dev.refresh()

dev.quit()