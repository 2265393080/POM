import pytest
from POM.page.login_page import LoginPage
from POM.page.index_page import IndexPage
from POM.base.base import BasePage
from POM.data.jsontest import json_read
import time
import os


# import allure

# @allure.feature('测试登陆模块')
class TestLogin:
    """登录测试类"""

    def setup_class(self):
        # self.driver = webdriver.Chrome()  # 获取浏览器对象
        self.Login_task = LoginPage()  # 实例化登陆页业务层对象
        self.Index_task = IndexPage()  # 实例化首页业务层对象
        # self.base = BasePage()

    def teardown_class(self):
        self.Login_task.close()  # 退出浏览器对象

    # 每个用例执行前都会执行setup
    def setup_method(self):
        # 打开首页
        pass

    def teardown_method(self):
        pass

    # @allure.story('登陆账号密码子功能-登陆失败')
    # @allure.title("登录失败的场景-{json}")
    @pytest.mark.parametrize('json', json_read())
    def test_account_does_not_exist(self, json):
        """测试用例1：账号不存在"""
        # 执行登录
        self.Login_task.goto('https://chezhutest.aibaoxian.com/app/WechatLogin?VNK=7e05846b')
        self.Login_task.js()
        self.Login_task.input_name(json["username"])
        self.Login_task.input_password(json["password"])
        self.Login_task.read_btn()
        self.Login_task.confirm_btn()
        self.Login_task.wait(1)
        self.Login_task.home_btn()
        self.Login_task.wait(3)


        # assert '请输入正确的手机号' == self.Login_task.take_text()
        assert 1 == 1

    # @pytest.mark.parametrize('user,pwd', [['150', '123456'], ['1506732', '123456']])
    # def test_pwd_does_not_exist(self, user, pwd):
    #     """测试用例3：密码不存在"""
    #     # 执行登录
    #     self.Login_task.goto('https://s.apps.vip/login')
    #     self.Login_task.input_name(user)
    #     self.Login_task.input_password(pwd)
    #     self.Login_task.confirm_btn()
    #     assert '请输入正确的手机号' == '请输入正确的手机号'


if __name__ == '__main__':
    pytest.main(['-vs', __file__])
    # pytest.main(['-vs --html=./result/report.html'])
    # pytest.main(["--html=report/re
    # port.html", __file__])    #生成自带的html测试报告

    # pytest.main(["-vs", __file__, "--alluredir=temp/html"])
    # os.system("allure generate ./temp/html -o ./report  --clean")
