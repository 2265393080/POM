import calendar
import time
from POM.utils.logger import log


class DateTimeUtil:
    def __init__(self):
        self.log = log

    def get_now_datetime(self):
        # 格式化输出当前时间
        try:
            now_datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            return now_datetime
        except Exception as e:
            self.log.error(e)

    def get_now_datetime_v2(self):
        # 格式化输出当前时间
        try:
            now_datetime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
            return now_datetime
        except Exception as e:
            self.log.error(e)

    def get_gmtime(self):
        # 获取当前时间戳
        try:
            return calendar.timegm(time.gmtime())
        except Exception as e:
            self.log.error(e)


if __name__ == '__main__':
    print(DateTimeUtil().get_now_datetime())
    print(DateTimeUtil().get_gmtime())
