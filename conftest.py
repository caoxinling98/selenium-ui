import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as CH_Options

#项目目录配置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = BASE_DIR + '/report/'
LOG_DIR = BASE_DIR + "/logs/"
IMG_DIR = BASE_DIR + "/screenshots/"
driver = None

#配置浏览器驱动类型（chrome/firefox/chrome-headless/firefox-headless）
driver_type = "chrome"

#配置运行的URL
url = "https://www.baidu.com"

#当达到最大失败数，停止运行
max_fail = '5'

#运行测试用例的目录或文件
cases_path = './testcases'


#基本测试环境
@pytest.fixture(scope='function')
def base_url():
    global url
    return url

def capture_screenshots(case_name):
#     """
#     配置用例失败截图路径
#     :param case_name: 用例名
#     :return:
#     """
    global driver
    file_name = case_name.split('/')[-1]
    new_report_dir = new_report_time()
    if new_report_dir is None:
        raise RuntimeError('没有初始化测试目录')
    image_dir = os.path.join(REPORT_DIR,new_report_dir,"image",file_name)
    driver.save_screenshot(image_dir)

def new_report_time():
    files = os.listdir(REPORT_DIR)
    files.sort()
    try:
        return files[-1]
    except IndexError:
        return None

#登录浏览器
@pytest.fixture(scope='session',autouse=True)
def login():
    global driver
    driver = webdriver.Chrome()
    return driver

#关闭浏览器
@pytest.fixture(scope='session',autouse=True)
def close():
    yield
    driver.quit()
    print('测试结束')