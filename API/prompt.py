from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome("../../chromedriver.exe")
driver.get("file:///D:/python/selenium_pages-master/alert.html")
alert1 = driver.find_element_by_id("b3").click()
time.sleep(2)
driver.switch_to.alert.send_keys("selenium")
Alert(driver).accept()
