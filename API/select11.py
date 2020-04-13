from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("../../chromedriver.exe")
driver.get("file:///D:/python/selenium_pages-master/form_web_element.html")
selects = Select(driver.find_element_by_id("ss_single")).options
assert len(selects) == 3,"个数不是3个"