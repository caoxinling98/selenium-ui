from selenium import webdriver
import time

driver = webdriver.Chrome("../../chromedriver.exe")
driver.get("file:///D:/python/selenium_pages-master/form_web_element.html")
radios = driver.find_elements_by_id('s_radio')
for radio in radios:
    print(radio.text)
# checked = driver.find_element_by_xpath('//div[@id="s_radio"]/input[@checked="checked"]').get_attribute('value')
# print(checked)
xiaolei = driver.find_element_by_xpath('//div[@id="s_radio"]/input[@value="小雷老师"]').click()