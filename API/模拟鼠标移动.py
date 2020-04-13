from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome("../../chromedriver.exe")
driver.get("https://www.baidu.com")
driver.maximize_window()
ele = driver.find_element_by_xpath("//a[@name='tj_briicon']")
print(ele.text)
time.sleep(2)
ActionChains(driver).move_to_element(ele).perform()