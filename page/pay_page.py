from POM.base.base import BasePage


class IndexPage(BasePage):
    def __init__(self):
        super().__init__()

        # 洗车相关按钮
        self.wash_car_icon = (
            'xpath', '//*[@id="home"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div')
        self.first_wash_car_business = ('xpath', '//*[@id="listWrap"]/li[1]/div/div[1]')

        # 保养相关按钮
        self.maintenance_icon = (
            'xpath', '//*[@id="home"]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[5]/div')
        self.first_maintenance_business = ('xpath', '//*[@id="listWrap"]/li[1]')
        self.brand = ('xpath', '//*[@id="safetyStoreWrap"]/div/div[5]/div/div[1]/div/div[2]/div/div[2]/div[1]/ul/li')
        self.liters = ('xpath', '//*[@id="safetyStoreWrap"]/div/div[5]/div/div[1]/div/div[2]/div/div[2]/div[2]/ul/li')

        # 公用按钮
        self.pay_button = ('xpath', '//*[@id="safetyStoreWrap"]/div/div[7]/div/div[2]/span')
        self.buy_button = ('xpath', '//*[@id="app"]/div[1]/div/div[2]/div/div[3]/span')
        self.pay_success_text = ('class name', 'van-button__text')

    # 点击“洗车”ICON
    def click_wash_car_icon(self):
        self.click(self.wash_car_icon)
        self.wait(5)

    # 点击洗车的第一家商户
    def click_first_business(self):
        self.click(self.first_wash_car_business)
        self.wait(5)

    # 点击立即购买按钮
    def click_pay_button(self):
        self.click(self.pay_button)
        self.wait(3)

    # 点击立即支付按钮
    def click_buy_button(self):
        self.click(self.buy_button)
        self.wait(3)

    # 获取“确认支付”的文本
    def get_pay_success_text(self):
        return self.get_text(self.pay_success_text)

    # 点击“保养”ICON
    def click_maintenance_icon(self):
        self.click(self.maintenance_icon)
        self.wait(3)

    # 点击保养的第一家商户
    def click_first_maintenance_business(self):
        self.click(self.first_maintenance_business)
        self.wait(5)

    # 点击选择品牌
    def click_brand(self):
        self.click(self.brand)
        self.wait(1)

    # 点击选择升数
    def click_liters(self):
        self.click(self.liters)
        self.wait(1)


if __name__ == '__main__':
    Index_task = IndexPage()
    Index_task.goto("https://chezhutest.aibaoxian.com/app/home?VNK=0053de14")
    Index_task.js()
    Index_task.refresh()
    Index_task.js()
    # Index_task.click_wash_car_icon()
    # Index_task.click_first_business()
    # Index_task.click_pay_button()
    # Index_task.click_buy_button()
    # Index_task.wait(3)
    # assert "确认支付" == Index_task.get_pay_success_text()
    # print("断言成功")
    # Index_task.wait(3)

    # 保养icon
    Index_task.click_maintenance_icon()
    Index_task.click_first_maintenance_business()
    Index_task.click_brand()
    Index_task.click_liters()
    Index_task.click_pay_button()
    Index_task.click_buy_button()
    Index_task.wait(3)
    assert "确认支付" == Index_task.get_pay_success_text()
    print("断言成功")
