#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/")
driver.implicitly_wait(30)
# （陷阱1：注意输入城市名前，一定要先点击一下输入框，否则查不到）
# （陷阱2：输入城市名最后要包含一个回车符，否则输入框里面会自动清除）
#出发地
driver.find_element_by_css_selector("#fromStationText").click()
fromStation = driver.find_element_by_css_selector("#fromStationText")
fromStation.send_keys("洪洞")
fromStation.send_keys(Keys.ENTER)
print(fromStation.get_attribute('value'))
#目的地
driver.find_element_by_css_selector("#toStationText").click()
toStation = driver.find_element_by_css_selector("#toStationText")
toStation.send_keys("北京")
toStation.send_keys(Keys.ENTER)
print(toStation.get_attribute('value'))
time.sleep(3)
#日期
date = driver.find_element_by_css_selector("#train_date")
js1 = "arguments[0].readOnly=false;arguments[0].value='2020-04-06';"
driver.execute_script(js1,date)
#查询
search = driver.find_element_by_css_selector("#search_one").click()

driver.switch_to(driver.window_handles[1])
text = driver.find_element_by_css_selector('')