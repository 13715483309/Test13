from mtxapi.api.Base_Api import Base_Api


class Mtx_Goodlist(Base_Api):

    def goodlislt(self,data):
        path = '/mtx/index.php?s=/index/search/goodslist.html'

        res = self.mtx_post(path,data)
        # print(res)
        return res

if __name__ == '__main__':
    obj = Mtx_Goodlist()
    obj.goodlislt()