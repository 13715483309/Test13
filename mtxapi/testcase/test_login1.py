import pytest

from mtxapi.api.Mtx_Login import Mtx_Login


class Test_login():

    def setup_class(self):
        self.logobj = Mtx_Login()

    #正向case
    @pytest.mark.parametrize('account,pwd',[('zhang','123456'),('li2','123456')])
    def test_login(self,account,pwd):
        res = self.logobj.login(account,pwd)
        assert res['msg'] == '登录成功'

    #密码不正确
    @pytest.mark.parametrize('account,pwd',[('zhang','234567')])
    def test_case2(self,account,pwd):
        res = self.logobj.login(account,pwd)
        assert res['msg'] == '密码错误'

    #用户名不存在
    @pytest.mark.parametrize('account,pwd',[('吗云','123456')])
    def test_case3(self,account,pwd):
        res = self.logobj.login(account,pwd)
        pytest.assume(res['msg'] == '帐号不存在')

    #密码位数不及6位或大于18位
    @pytest.mark.parametrize('account,pwd',[('zhang','1234'),('zhang','12345678909876543212345')])
    def test_case4(self,account,pwd):
        res = self.logobj.login(account,pwd)
        pytest.assume(res['msg']=='密码格式 6~18 个字符之间')
        pytest.assume(res['code'] == -2)



if __name__ == '__main__':
    pytest.main(['-s'])