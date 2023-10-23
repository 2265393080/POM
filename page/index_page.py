from POM.base.base import BasePage


class IndexPage(BasePage):
    def __init__(self):
        super().__init__()
        self.my = ('xpath', '//*[@id="app"]/div[2]/div[5]')

    # 点击“我的”页面
    def my_btn(self):
        self.click(self.my)
        self.wait(1)


if __name__ == '__main__':
    Index_task = IndexPage()
    Index_task.goto('https://chezhutest.aibaoxian.com/app/home?VNK=1323ebd7')
    Index_task.js()
    Index_task.my_btn()
    Index_task.wait(3)
