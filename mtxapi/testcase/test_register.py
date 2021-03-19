import pytest

from mtxapi.api.Mtx_Register import Mtx_Register


class Test_Register():

    def setup_class(self):
        self.regobj = Mtx_Register()

    @pytest.mark.parametrize('account,pwd,type,is_agree',[('li46','123456','username',1)])
    def test_case_01(self,account,pwd,type,is_agree):
        data = {
            'accounts': account,
            'pwd': pwd,
            'type': type,
            'is_agree_agreement': is_agree
        }
        res = self.regobj.register(data)
        print(res)
        pytest.assume(res['msg'] == '注册成功')
        pytest.assume(res['code'] == 0)

    @pytest.mark.parametrize('account,pwd,type,is_agree', [('li43', '123456', 'username', 1)])
    def test_case_02(self, account, pwd, type, is_agree):
        data = {
            'accounts': account,
            'pwd': pwd,
            'type': type,
            'is_agree_agreement': is_agree
        }
        res = self.regobj.register(data)
        print(res)
        pytest.assume(res['msg'] == '账号已存在')
        pytest.assume(res['code'] == -10)

if __name__ == '__main__':
    pytest.main(['-s'])