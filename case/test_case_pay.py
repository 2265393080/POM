import pytest
from POM.page.pay_page import IndexPage
from POM.data.jsontest import json_read
import time
import os


# import allure

class TestLogin:
    """登录测试类"""

    def setup_class(self):
        self.Index_task = IndexPage()  # 实例化首页业务层对象

    def teardown_class(self):
        self.Index_task.close()  # 退出浏览器对象

    # 每个用例执行前都会执行setup
    def setup_method(self):
        # 打开首页
        pass

    def teardown_method(self):
        pass

    def test_payment_wash_car_success(self, ):
        """测试用例1：洗车->收银台 跳转成功"""
        # 执行登录
        self.Index_task.goto("https://chezhutest.aibaoxian.com/app/home?VNK=0053de14")
        self.Index_task.js()
        self.Index_task.refresh()
        self.Index_task.js()
        self.Index_task.click_wash_car_icon()
        self.Index_task.click_first_car_business()
        self.Index_task.click_buy_button()
        self.Index_task.click_pay_button()
        self.Index_task.wait(3)
        assert "确认支付" == self.Index_task.get_pay_success_text()
        print("断言成功")

    def test_payment_maintenance_success(self, ):
        """测试用例2：保养->收银台 跳转成功"""
        # 执行登录
        self.Index_task.goto("https://chezhutest.aibaoxian.com/app/home?VNK=0053de14")
        self.Index_task.js()
        self.Index_task.refresh()
        self.Index_task.js()
        self.Index_task.click_maintenance_icon()
        self.Index_task.click_first_maintenance_business()
        self.Index_task.click_brand()
        self.Index_task.click_liters()
        self.Index_task.click_buy_button()
        self.Index_task.click_pay_button()
        self.Index_task.wait(3)
        assert "确认支付" == self.Index_task.get_pay_success_text()
        print("断言成功")


if __name__ == '__main__':
    pytest.main(['-vs', __file__])

    # pytest.main([__file__, '-vs', '--alluredir', '../result/allurejson', '--clean-alluredir'])
    # os.system("allure generate ../result/allurejson -o ../result/report --clean")
    # os.system("allure open ../result/report")
