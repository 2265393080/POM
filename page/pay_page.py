from POM.base.base import BasePage


class PayPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

        # 洗车相关按钮
        self.wash_car_icon = ('xpath', '//p[.="洗车"]/parent::div')
        self.first_car_business = ('css selector', '#listWrap > li:nth-child(1) > div > div.cell-item')  # 列表内第一个商家
        # 保养相关按钮
        self.maintenance_icon = ('xpath', '//p[.="机油保养"]/parent::div')
        self.brand = ('xpath', '//*[@id="safetyStoreWrap"]/div/div[5]/div/div[1]/div/div[2]/div/div[2]/div[1]/ul/li')
        self.liters = ('xpath', '//*[@id="safetyStoreWrap"]/div/div[5]/div/div[1]/div/div[2]/div/div[2]/div[2]/ul/li')
        self.first_maintenance_business = ('css selector', '#listWrap > li:nth-child(1)')  # 列表内第一个商家
        # 公用按钮
        self.buy_button = ('css selector', 'div.pay_btn > span')  # 立即购买
        self.pay_button = ('css selector', 'div.pay_btn > span')  # 立即支付
        self.pay_success_text = ('class name', 'van-button__text')

    # 点击“洗车”ICON
    def click_wash_car_icon(self):
        self.click(self.wash_car_icon)
        self.wait(3)

    # 点击洗车的第一家商户
    def click_first_car_business(self):
        self.click(self.first_car_business)
        self.wait(3)

    # 点击立即购买按钮
    def click_buy_button(self):
        self.click(self.buy_button)
        self.wait(3)

    # 点击立即支付按钮
    def click_pay_button(self):
        self.click(self.pay_button)
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
        self.wait(3)

    # 点击选择品牌
    def click_brand(self):
        self.click(self.brand)
        self.wait(1)

    # 点击选择升数
    def click_liters(self):
        self.click(self.liters)
        self.wait(1)


if __name__ == '__main__':
    Index_task = PayPage()
    Index_task.goto("https://chezhutest.aibaoxian.com/app/home?VNK=0053de14")
    Index_task.js_init()
    Index_task.refresh()
    Index_task.js_init()
    # Index_task.click_wash_car_icon()
    # Index_task.click_first_car_business()
    # Index_task.click_buy_button()
    # Index_task.click_pay_button()
    # Index_task.wait(3)
    # assert "确认支付" == Index_task.get_pay_success_text()
    # print("断言成功")
    # Index_task.wait(3)

    # 保养icon
    Index_task.click_maintenance_icon()
    Index_task.click_first_maintenance_business()
    Index_task.click_brand()
    Index_task.click_liters()
    Index_task.click_buy_button()
    Index_task.click_pay_button()
    Index_task.wait(3)
    assert "确认支付" == Index_task.get_pay_success_text()
    print("断言成功")
