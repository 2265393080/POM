"""
@名称:    base.py
@作者:    XZY
@时间:    2022/12/25 20:43
@描述:    BasePage类是POM中的基类，主要用于提供常用的函数，为页面对象类进行服务
"""

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
        self.driver.implicitly_wait(2)

    def js(self):
        self.driver.execute_script("localStorage.setItem('channel', '10')")
        self.driver.execute_script('sessionStorage.setItem("openId", "1111")')
        self.driver.execute_script('sessionStorage.setItem("city", "嘉兴")')
        self.driver.execute_script('sessionStorage.setItem("AdCode", "330400")')
        self.driver.execute_script('sessionStorage.setItem("Coordinate", "120.687948, 30.757605")')
        element = self.driver.find_elements(By.XPATH, '/html/div')
        self.driver.execute_script("arguments[0].style = 'display:none';", element[0])

    # 访问URL
    def goto(self, url):
        self.driver.get(url)

    # 元素定位
    def locator(self, *loc):
        try:
            return WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(*loc))
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


# 测试用
if __name__ == '__main__':
    test = BasePage()
    test.goto('https://chezhutest.aibaoxian.com/app/WechatLogin?VNK=7e05846b')
    test.wait(1)
    test.js()
    # test.locator(('class name', 'secondary'))

    test.click(('xpath', '//*[@id="__layout"]/div/div[4]/div/div[3]/div[1]/form/div[3]/div/button'))
    test.wait(1)
    # a = test.get_text(('class name', 'error'))
    # print(a)
