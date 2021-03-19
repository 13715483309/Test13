import pytest


class test_case():
    def test_case1(self):
        print('124')

    def test_case2(self):
        print('908')


if __name__ == '__main__':
    pytest.main(['-s'])
