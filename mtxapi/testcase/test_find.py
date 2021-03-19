import pytest

from mtxapi.api.Mtx_Find import Mtx_Find


class Test_Find():

    def setup_class(self):
        self.findobj = Mtx_Find()

    @pytest.mark.parametrize('kw',(['手机']))
    def test_case_1(self,kw):
        data = {
            'wd': kw
        }
        res = self.findobj.find(data)
        assert '手机' in res

if __name__ == '__main__':
    pytest.main(['-s'])