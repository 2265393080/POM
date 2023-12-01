import logging
import os
import datetime

class Log:
    def __init__(self):
        self.logger = logging.getLogger()
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            log_dir = os.path.join(BASE_DIR, "logs")
            # 创建日志路径
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            log_file = os.path.join(log_dir, "{}.log".format(datetime.datetime.now().strftime("%Y%m%d")))

            # 创建一个handle写入文件
            fh = logging.FileHandler(log_file, encoding="utf-8")
            fh.setLevel(logging.INFO)

            # 创建一个handle输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # 定义输出的格式
            formatter = logging.Formatter(self.fmt)
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 添加到handle
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    @property
    def fmt(self):
        return "%(levelname)s\t%(asctime)s\t[%(filename)s:%(lineno)d]\t%(message)s"


log = Log().logger

if __name__ == "__main__":
    log.info("info")
    log.error("error")
    log.warning("warn")
