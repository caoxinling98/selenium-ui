#coding=utf-8
import logging
import time
from conftest import LOG_DIR


class Logger(object):
    def __init__(self,logger):

        #创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #创建一个handler，写入日志文件
        create_time = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_name = LOG_DIR + create_time + '.log'
        file_handler = logging.FileHandler(log_name)
        file_handler.setLevel(logging.INFO)

        # 创建一个handler，写入控制台
        console_handler = logging.StreamHandler(stream=None)
        console_handler.setLevel(logging.INFO)

        #定义日志格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        #给logger添加handler
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def getlog(self):
        return self.logger
