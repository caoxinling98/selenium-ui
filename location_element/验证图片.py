from selenium import webdriver

driver=webdriver.Chrome("D:/python/chromedriver.exe")
driver.get("http://v3.alphacoding.cn")
img=driver.find_element_by_id("info-image")