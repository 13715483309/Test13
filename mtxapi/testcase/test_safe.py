import pytest

from mtxapi.api.Mtx_Login import Mtx_Login
from mtxapi.api.Mtx_Safe import Mtx_Safe
from mtxapi.log.Logger import Logger


class Test_Safe():

    def setup_class(self):
        self.loginobj = Mtx_Login()
        self.logerobj = Logger().get_logger()
        self.safeobj = Mtx_Safe()

    #登录
    @pytest.mark.parametrize('account,pwd',[('li40','123456')])
    def test_login(self,account,pwd):
        res = self.loginobj.login(account,pwd)
        pytest.assume(res['msg'] == '登录成功')
        self.logerobj.info('登录操作')

    #正向case
    @pytest.mark.parametrize('my,new,confirm',[('123456','123456','123456')])
    def test_safe(self,my,new,confirm):
        res = self.safeobj.safe(my,new,confirm)
        pytest.assume(res['msg']=='修改成功')
        pytest.assume(res['code']==0)
        self.logerobj.info('修改密码')

    # 密码错误
    @pytest.mark.parametrize('my,new,confirm',[('234567','123456','123456')])
    def test_safe_pwdisfalse(self,my,new,confirm):
        res = self.safeobj.safe(my,new,confirm)
        pytest.assume(res['msg']=='当前密码错误')
        pytest.assume(res['code']==-4)
        self.logerobj.info('密码错误')

if __name__ == '__main__':
    pytest.main(['-s'])