#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
import time
import win32api
import win32con

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
driver.maximize_window()
mainWindow = driver.current_window_handle
time.sleep(2)
#更多产品
more_elements = driver.find_element_by_name("tj_briicon")
#鼠标移到“更多产品”
# ac = ActionChains(driver)
ActionChains(driver).move_to_element(more_elements).perform()
time.sleep(2)

#点击图片

img_element = driver.find_element_by_xpath("//a[@name='tj_img']")
ActionChains(driver).move_to_element(img_element).click().perform()
#定位百度图片输入框，并输入内容“笔记本电脑”
input_element = driver.find_element_by_id("kw").send_keys('笔记本电脑')
#点击搜索
search_button = driver.find_element_by_class_name('s_search').click()
# print(driver.current_url)
# driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
#定位到要右击的元素
pc_img_element = driver.find_element_by_xpath("//a[@name='pn1']")
ActionChains(driver).context_click(pc_img_element).perform()
time.sleep(2)
# try:
#     pc_img_element = driver.find_element_by_xpath("//a[@name='pn1']")
# except exceptions.StaleElementReferenceException as msg:
#     print('查找元素异常'+msg)
#     print('重新获取元素')
#     pc_img_element = driver.find_element_by_xpath("//a[@name='pn1']")
#
# try:
#     ActionChains(driver).context_click(pc_img_element).perform()
# except exceptions.StaleElementReferenceException as e:
#     print(e)
#     print('chongadjfdfasfasfs')
#     ActionChains(driver).context_click(pc_img_element).perform()
# time.sleep(2)
#点击v图片另存为：
#按下键盘上的v键
win32api.keybd_event(86,0,0,0)
#释放
win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)

time.sleep(5)
driver.close()


