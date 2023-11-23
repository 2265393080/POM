import pytest
from POM.page.pay_page import PayPage
import allure
import os


@allure.feature('测试支付模块')
class TestLogin:
    @allure.story('支付子功能：收银台跳转成功')
    @allure.title('测试用例1：洗车->收银台 跳转成功')
    def test_payment_wash_car_success(self, browser):
        # 执行登录
        Pay_task = PayPage(browser)
        Pay_task.goto("https://chezhutest.aibaoxian.com/app/home?VNK=0053de14")
        Pay_task.js_init()
        Pay_task.refresh()
        Pay_task.js_init()
        Pay_task.click_wash_car_icon()
        Pay_task.click_first_car_business()
        Pay_task.click_buy_button()
        Pay_task.click_pay_button()
        Pay_task.wait(3)
        assert "确认支付" == Pay_task.get_pay_success_text()
        print("断言成功")

    @allure.story('支付子功能：收银台跳转成功')
    @allure.title('测试用例1：保养->收银台  跳转成功')
    def test_payment_maintenance_success(self, browser):
        Pay_task = PayPage(browser)
        Pay_task.goto("https://chezhutest.aibaoxian.com/app/home?VNK=0053de14")
        Pay_task.js_init()
        Pay_task.refresh()
        Pay_task.js_init()
        Pay_task.click_maintenance_icon()
        Pay_task.click_first_maintenance_business()
        Pay_task.click_brand()
        Pay_task.click_liters()
        Pay_task.click_buy_button()
        Pay_task.click_pay_button()
        Pay_task.wait(3)
        assert "确认支付" == Pay_task.get_pay_success_text()
        print("断言成功")


if __name__ == '__main__':
    pytest.main(['-vs', __file__])
    # pytest.main([__file__, '-vs', '--alluredir', '../result/allurejson', '--clean-alluredir'])
    # os.system("allure generate ../result/allurejson -o ../result/report --clean")
    # os.system("allure open ../result/report")
