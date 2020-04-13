from selenium import webdriver
import time
driver = webdriver.Chrome('../../chromedriver.exe')
driver.get("http://news.baidu.com/")
num=1
while num<10:
    time.sleep(1)
    driver.refresh()
