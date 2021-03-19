import pytest

from ios.page.Contacts_Search import Contancts_Search


class Test_contacts_search():

    def setup_class(self):
        self.searchobj = Contancts_Search()

    def test_case_1(self):
        self.searchobj.search()

if __name__ == '__main__':
    pytest.main(['-s'])