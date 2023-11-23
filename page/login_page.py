from POM.base.base import BasePage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.name = ('xpath', '//*[@id="app"]/div[1]/div/div[2]/div[3]/div[1]/input')  # 账号
        self.pwd = ('xpath', '//*[@id="app"]/div[1]/div/div[2]/div[4]/div[1]/div[1]/input')  # 密码
        self.read = ('class name', 'Read')  # 同意按钮
        self.btn = ('class name', 'loginBtn')  # 登录按钮
        self.home = ('class name', 'icon-back-home')  # 右上角home图标
        self.footerLogin = ('xpath', '//*[@id="home"]/div[3]/div[2]')  # 首页底部的登录入口

    # 输入账号
    def input_name(self, username):
        self.send_keys(self.name, username)
        self.wait(1)

    # 输入密码
    def input_password(self, pwd):
        self.send_keys(self.pwd, pwd)
        self.wait(1)

    # 点击同意按钮
    def read_btn(self):
        self.click(self.read)
        self.wait(1)

    # 点击登录按钮
    def confirm_btn(self):
        self.click(self.btn)
        self.wait(1)

    # 文本是否存在
    def text_is_exist(self):
        return self.is_element_exist(self.footerLogin)

    # 点击home按钮
    def home_btn(self):
        self.click(self.home)
        self.wait(1)


if __name__ == '__main__':
    test = LoginPage(webdriver)
    mobile_emulation = {"deviceName": "iPhone 6"}
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    test.driver = webdriver.Chrome(options=options)
    test.driver.maximize_window()
    test.driver.implicitly_wait(3)
    test.goto('https://chezhutest.aibaoxian.com/app/WechatLogin?VNK=7e05846b')
    test.js_init()

    # test.input_name("15067327230")
    # test.input_password("123456")
    # test.read_btn()
    # test.confirm_btn()
    # test.wait(3)
    test.home_btn()
    test.wait(30)
