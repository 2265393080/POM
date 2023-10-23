from POM.base.base import BasePage


class LoginPage(BasePage):
    def __init__(self):
        self.name = ('xpath', '//*[@id="app"]/div[1]/div/div[2]/div[3]/div[1]/input')  # 账号
        self.pwd = ('xpath', '//*[@id="app"]/div[1]/div/div[2]/div[4]/div[1]/div[1]/input')  # 密码
        self.read = ('class name', 'Read')  # 同意按钮
        self.btn = ('class name', 'loginBtn')  # 登录按钮
        self.home = ('class name', 'icon-back-home')  # 右上角home图标

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

    # 获取文本
    # def take_text(self):
    #     return self.get_text(self.text)

    # 点击home按钮
    def home_btn(self):
        self.click(self.home)
        self.wait(1)


if __name__ == '__main__':
    test = LoginPage()
    test.goto('https://chezhutest.aibaoxian.com/app/WechatLogin?VNK=7e05846b')
    test.js()
    test.wait(1)
    test.input_name("15067327230")
    test.input_password("123456")
    test.read_btn()
    test.confirm_btn()
    test.wait(3)
    test.home_btn()
    test.wait(3)