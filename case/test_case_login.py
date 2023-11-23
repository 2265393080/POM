import pytest
from POM.data.jsontest import json_read
from POM.page.login_page import LoginPage
import allure
import os


@allure.feature('测试登陆模块')
class TestLogin:
    @allure.story('登陆账号密码子功能-登陆失败')
    @allure.title('测试用例1：账号不存在')
    @pytest.mark.parametrize('json', json_read())
    def test_account_does_not_exist(self, json, browser):
        Login_task = LoginPage(browser)
        Login_task.goto('https://chezhutest.aibaoxian.com/app/WechatLogin?VNK=7e05846b')
        Login_task.js_init()
        Login_task.input_name(json["username"])
        Login_task.input_password(json["password"])
        Login_task.read_btn()
        Login_task.confirm_btn()
        Login_task.wait(1)
        Login_task.home_btn()
        Login_task.wait(3)
        print(Login_task.text_is_exist())
        assert True == Login_task.text_is_exist()  # noqa

    # @pytest.mark.parametrize('user,pwd', [['150', '123456'], ['1506732', '123456']])
    # def test_pwd_does_not_exist(self, browser, user, pwd):
    #     """测试用例3：密码不存在"""
    #     # 执行登录
    #     Login_task = LoginPage(browser)
    #     Login_task.goto('https://chezhutest.aibaoxian.com/app/WechatLogin?VNK=7e05846b')
    #     Login_task.input_name(user)
    #     Login_task.input_password(pwd)
    #     Login_task.confirm_btn()
    #     assert '请输入正确的手机号' == '请输入正确的手机号'


if __name__ == '__main__':
    pytest.main(['-vs', __file__])
    # pytest.main([__file__, '-vs', '--alluredir', '../result/allurejson', '--clean-alluredir'])
    # os.system("allure generate ../result/allurejson -o ../result/report --clean")
    # os.system("allure open ../result/report")
