import pytest

from mtxapi.api.Mtx_Login import Mtx_Login
from mtxapi.api.Mtx_PersonalSave import Mtx_PersonalSave
from mtxapi.log.Logger import Logger


class Test_PersonalSave():

    def setup_class(self):
        self.loginobj = Mtx_Login()
        self.perobj = Mtx_PersonalSave()
        self.getlogger = Logger().get_logger()
        self.getlogger.info('个人信息初始化')

    #登录
    @pytest.mark.parametrize('account,pwd',[('li40','123456')])
    def test_case_1(self,account,pwd):
        res = self.loginobj.login(account,pwd)
        assert res['msg'] == '登录成功'
        self.getlogger.info('登录')

    @pytest.mark.parametrize('nickname,gender,birthday',[('li40',2,'2015-09-12')])
    def test_case_2(self,nickname,gender,birthday):
        data = {
            'nickname': nickname,
            'gender': gender,
            'birthday': birthday
        }
        res = self.perobj.persave(data)
        assert res['msg'] == '编辑成功'
        self.getlogger.info('编辑个人信息')

    @pytest.mark.parametrize('nickname,gender,birthday', [('', '', '')])
    def test_case_3(self, nickname, gender, birthday):
        data = {
            'nickname': nickname,
            'gender': gender,
            'birthday': birthday
        }
        res = self.perobj.persave(data)
        print(res)
        assert res['msg'] == '编辑成功'
        self.getlogger.info('错误编辑个人信息')


if __name__ == '__main__':
    pytest.main(['-s'])