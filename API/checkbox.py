from selenium import webdriver
import time

driver = webdriver.Chrome("../../chromedriver.exe")
driver.get("file:///D:/python/selenium_pages-master/form_web_element.html")
checks = driver.find_elements_by_id('s_checkbox')
for check in checks:
    if check.find_element_by_xpath("//div[2]/input[@checked='checked']").is_selected():
        print(1)
        check.find_element_by_xpath("//div[2]/input[@checked='checked']").click()
try:
    assert (driver.find_element_by_xpath('//div[2]/input[@checked="checked"]').is_selected()),'复选框未被选中'
except AssertionError as msg:
    print(msg)
xiaolei = driver.find_element_by_xpath('//div[2]/input[@value="小雷老师"]').click()
