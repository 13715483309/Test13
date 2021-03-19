from httprunner import HttpRunner,Config,Step,RunRequest,RunTestCase

from httprunner3.dir_test.testcases.http_str import Test_htun_stu


class stu_run_testcase(HttpRunner):

    config = Config('导入其他测试的例子').base_url('http:127.0.0.1')

    teststeps = [
        Step(
            RunTestCase('引入case')
            .call(Test_htun_stu)
            .export(*['var_username'])
        ),
        Step(
            RunRequest('调用接口')
            .get('/string_data')
            .with_params(**{'data':'$var_username'})
        )
    ]

if __name__ == '__main__':
    stu_run_testcase.test_start()