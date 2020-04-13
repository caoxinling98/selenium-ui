from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome("../../chromedriver.exe")
driver.get("file:///D:/python/selenium_pages-master/alert.html")
alert1 = driver.find_element_by_id("b2").click()
time.sleep(2)
Alert(driver).accept()
alert1 = driver.find_element_by_id("b2").click()
time.sleep(2)
Alert(driver).dismiss()
