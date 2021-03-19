from httprunner import HttpRunner,Config,Step,RunRequest,RunTestCase
import pytest
class Test_htun_stu(HttpRunner):
    @pytest.mark.parametrize("")
    config = Config('用来学习的case').base_url('http://127.0.0.1:5000')

    teststeps = [
        Step(
            RunRequest('测试case')#新写一个case
            .get('/getuserName')
            .extract()
            .with_jmespath('body.username','var_username')
            # RunTestCase#
        ),
        Step(
            RunRequest('测试joinstr接口')
            .get('/jsonstr')
            .with_params(**{'str1':'helli','str2':'$var_username'})
            .validate()
            .assert_equal('body.result', 'hello $var_username')

        )
    ]

if __name__ == '__main__':
    Test_htun_stu().test_start()