import pytest
from selenium import webdriver

from mtxweb.page.Mtx_Answers import Mtx_Answers
from mtxweb.page.Mtx_Left import Mtx_Left
from mtxweb.page.Mtx_Login import Mtx_Login
from mtxweb.tools.log import Logger


class Test_Answers():

    def setup_class(self):
        self.dev = webdriver.Chrome()
        self.loginobj = Mtx_Login(self.dev)
        self.leftobj = Mtx_Left(self.dev)
        self.loggerobj = Logger().get_logger()
        self.answerobj = Mtx_Answers(self.dev)
        self.loggerobj.info('初始化')

    def test_login(self):
        try:
            self.loginobj.login()
            self.loggerobj.info('登录成功')
        except Exception as e:
            self.loggerobj.warn(f'出错{e}')


    def test_goto_answers(self):
        try:
            self.leftobj.myshopt()
            self.leftobj.answers()
            self.loggerobj.info('页面跳转')
        except Exception as e:
            self.loggerobj.warn(f'出错了{e}')

    def test_answers(self):
        try:
            self.answerobj.answers()
            self.loggerobj.info('问答页面')
        except Exception as e:
            self.loggerobj.warn(f'出错了{e}')

    def teardown_class(self):
        self.dev.quit()

if __name__ == '__main__':
    pytest.main(['-s'])