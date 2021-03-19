import pytest

from mtxapi.api.Mtx_Addadress import Mtx_Addadress
from mtxapi.api.Mtx_Login import Mtx_Login


class Test_Addaddress():

    def setup_class(self):
        self.logobj = Mtx_Login()
        self.addobj = Mtx_Addadress()

    @pytest.mark.parametrize('accounts,pwd',[('zhang','123456')])
    def test_case1(self,accounts,pwd):
        res = self.logobj.login(accounts,pwd)
        print(res)
        pytest.assume(res['msg']=='登录成功')

    @pytest.mark.parametrize('name,tel,address,id,province,city,county,is_default',\
                             [('li','137123212321','动车98号','',6,112,1567,0)])
    def test_case2(self,name,tel,address,id,province,city,county,is_default):
        data = {
            'name': name,
            'tel': tel,
            'address': address,
            'id': id,
            'province': province,
            'city': city,
            'county': county,
            'is_default': is_default
        }
        res = self.addobj.address(data)
        print(res)
        pytest.assume(res['msg']=='新增成功')

if __name__ == '__main__':
    pytest.main(['-s'])
