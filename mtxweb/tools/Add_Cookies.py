from time import sleep

class Add_Cookies():

    def adcook(self, dev):
        dev.get("http://121.42.15.146:9090/mtx/")
        sleep(2)
        dev.add_cookie({'name': 'PHPSESSID', 'value': 'o37s9ebl10ui1s15hcglfl55h6'})
        sleep(2)
        dev.refresh()
        dev.implicitly_wait(10)