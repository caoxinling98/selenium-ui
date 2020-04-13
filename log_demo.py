import logging

#获取一个logger对象
logger = logging.getLogger()
#日志级别
logger.setLevel(logging.ERROR)

#创建一个handler,输出到一个File文件/控制台
# file_path = logging.FileHandler
# logger.addHandler(file_path)
console = logging.StreamHandler()
logger.addHandler(console)

#定义formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(leverlname)s - %(message)s')

#为handler添加formatter
console.setFormatter(formatter)
