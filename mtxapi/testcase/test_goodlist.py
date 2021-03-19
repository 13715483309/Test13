import pytest

from mtxapi.api.Mtx_Goodlist import Mtx_Goodlist
from mtxapi.log.Logger import Logger


class Test_Goodlist():

    def setup_class(self):
        self.goodobj = Mtx_Goodlist()
        self.logobj = Logger().get_logger()

    @pytest.mark.parametrize('id,wd,page,field,type',[(59,'',1,'default','asc')])
    def test_case_1(self,id,wd,page,field,type):
        data = {
            'category_id': id,
            'wd': wd,
            'page': page,
            'order_by_field': field,
            'order_by_type': type
        }
        res = self.goodobj.goodlislt(data)
        # pytest.assume(res['msg']=='没有更多数据啦')
        # pytest.assume(res['code'] == -100)
        if res['code']==-100:
            pytest.assume(res['msg']=='没有更多数据啦')
            self.logobj.info(f'category_id:{id}没有更多数据了')
        elif res['code'] == 0:
            pytest.assume(res['msg'] == '处理成功')
            self.logobj.info(f'category_id:{id}处理成功')

    @pytest.mark.parametrize('id,wd,page,field,type',[(69,'',1,'default','asc')])
    def test_case_2(self,id,wd,page,field,type):
        data = {
            'category_id': id,
            'wd': wd,
            'page': page,
            'order_by_field': field,
            'order_by_type': type
        }
        res = self.goodobj.goodlislt(data)
        if res['code']==-100:
            pytest.assume(res['msg']=='没有更多数据啦')
            self.logobj.info(f'category_id:{id}没有更多数据了')
        elif res['code'] == 0:
            pytest.assume(res['msg'] == '处理成功')
            self.logobj.info(f'category_id:{id}处理成功')



if __name__ == '__main__':
    pytest.main(['-s'])