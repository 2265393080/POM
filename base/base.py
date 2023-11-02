from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class BasePage:

    def __init__(self):

        # 设置手机模式
        mobile_emulation = {"deviceName": "iPhone 6"}
        options = Options()
        options.add_experimental_option("mobileEmulation", mobile_emulation)
        # options.add_argument("--auto-open-devtools-for-tabs")  #开发者模式

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def js(self):
        self.driver.execute_script("localStorage.setItem('channel', '10')")
        self.driver.execute_script('sessionStorage.setItem("openId", "1111")')
        self.driver.execute_script('sessionStorage.setItem("city", "嘉兴")')
        self.driver.execute_script('sessionStorage.setItem("AdCode", "330400")')
        self.driver.execute_script('sessionStorage.setItem("Coordinate", "120.687948, 30.757605")')
        # 关闭页面上的vConsole
        element = self.driver.find_elements(By.XPATH, '/html/div')
        if element:
            self.driver.execute_script("arguments[0].style = 'display:none';", element[0])
        # 存入用户token
        self.driver.execute_script(
            "localStorage.setItem('token', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiMCIsInVuaXF1ZV9waG9uZSI6IjE1MDAwMDAwMDAwIiwidXNlcklkIjoiMTM1MjU2MyIsImlzcyI6InJlc3RhcGl1c2VyIiwiYXVkIjoiMDk4ZjZiY2Q0NjIxZDM3M2NhZGU0ZTg2NDI2NGI0ZjgifQ.Efmr5Mp-iEB48TIZLrED3J3JKsaPtYLzi7tGdfVSEeE')")

    # 访问URL
    def goto(self, url):
        self.driver.get(url)

    # 元素定位
    def locator(self, *loc):
        try:
            return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(*loc))
        except Exception as msg:
            print("定位的元素异常%s" % msg)

    # 输入
    def send_keys(self, loc, value, clear_first=True):
        element = self.locator(loc)
        if clear_first:
            element.clear()
            element.send_keys(value)
        else:
            element.send_keys(value)

    # 点击
    def click(self, loc):
        try:
            return self.locator(loc).click()
        except Exception as msg:
            print("无法点击到该元素" % msg)

    # 等待
    def wait(self, time):
        sleep(time)

    # 关闭
    def close(self):
        self.driver.quit()

    # 获取文本
    def get_text(self, loc):
        return self.locator(loc).text

    # 刷新页面
    def refresh(self):
        return self.driver.refresh()


# 测试用
if __name__ == '__main__':
    test = BasePage()
    test.goto('https://chezhutest.aibaoxian.com/app/WechatLogin?VNK=7e05846b')
    test.js()
    test.wait(1)
