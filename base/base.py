import time
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from POM.utils.logger import log
from POM.utils.get_path import GetPathInfo
from POM.utils.datetime_ import DateTimeUtil


class BasePage:
    def __init__(self, driver):
        self.time = DateTimeUtil()
        self.driver = driver
        self.log = log

    # 初始化操作
    def js_init(self):
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
        log.info("执行js初始化操作")

    # 执行js代码
    def execute(self, jsScript):
        self.driver.execute_script(jsScript)

    # 访问URL
    def goto(self, url):
        self.driver.get(url)
        log.info("打开网页：%s" % url)

    # 元素定位
    def locator(self, *loc):
        try:
            return WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(*loc))
        except Exception as msg:
            log.error("定位元素{}超时".format(loc), msg)

    # 判断元素是否存在
    def is_element_exist(self, args):
        flag = True
        try:
            self.locator(args)
            return flag
        except Exception as msg:
            flag = False
            log.error("判断元素{}存在异常".format(args), msg)
            return flag

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
            log.error("元素{}无法点击".format(loc), msg)

    # 等待
    def wait(self, times):
        time.sleep(times)
        log.info("等待{}s".format(times))

    # 关闭浏览器
    def close(self):
        self.driver.quit()
        log.info("关闭浏览器")

    # 获取文本
    def get_text(self, loc):
        text = self.locator(loc).text
        log.info("元素{}的文本为{}".format(loc, text))
        return text

    # 获取元素属性值
    def get_attribute(self, loc, attribute_values):
        value = self.locator(loc).get_attribute(attribute_values)
        log.info("元素{}的属性值为{}".format(loc, value))
        return value

    # 刷新页面
    def refresh(self):
        log.info("刷新页面")
        return self.driver.refresh()

    # 保存截图
    def save_screenshot_(self, pic_name):
        try:
            # 图片命名：元素名称-年-月-日-时-分-秒.png
            screenshot_path = GetPathInfo().get_project_path() + r"screenshots"
            if not os.path.exists(screenshot_path):
                os.makedirs(screenshot_path)
            file_name = screenshot_path + "/{}_{}.png".format(self.time.get_now_datetime_v2(), pic_name)
            self.driver.get_screenshot_as_file(file_name)
            log.info("成功截图保存到{}".format(file_name))
        except Exception:
            log.error("截图失败")
            raise


if __name__ == '__main__':
    test = BasePage(webdriver)

    # 设置手机模式
    mobile_emulation = {"deviceName": "iPhone 6"}
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    # 开发者模式
    # options.add_argument("--auto-open-devtools-for-tabs")

    test.driver = webdriver.Chrome(options=options)
    test.driver.maximize_window()
    test.driver.implicitly_wait(3)
    test.goto('https://chezhutest.aibaoxian.com/app/WechatLogin?VNK=7e05846b')
    test.js_init()
    test.wait(2)
    test.save_screenshot_('12345')
