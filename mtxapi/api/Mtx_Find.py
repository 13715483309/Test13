from mtxapi.api.Base_Api import Base_Api


class Mtx_Find(Base_Api):

    def find(self,data):
        path = '/mtx/index.php?s=/index/search/index.html'

        res = self.mtx_post(path,data)
        return res

if __name__ == '__main__':
    obj = Mtx_Find()
    obj.find()
