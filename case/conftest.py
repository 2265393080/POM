import os
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture(scope="session")
def browser():
    # 设置浏览器驱动
    mobile_emulation = {"deviceName": "iPhone 6"}
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(3)

    # 在测试运行前执行操作
    yield driver

    # 在测试运行后执行操作
    driver.quit()


# 如果需要在每个测试用例中共享一些数据，可以在这里定义 fixture
# 例如，你可以在这里设置登录逻辑，并返回登录后的用户对象
@pytest.fixture(scope="function")
def logged_in_user(browser):
    # 登录逻辑...
    user = {"username": "test_user", "email": "test@example.com"}
    return user

# 在这里定义其他的 fixture 或全局的 pytest 钩子函数
