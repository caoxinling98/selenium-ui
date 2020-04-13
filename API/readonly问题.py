#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://v3.alphacoding.cn/login")
driver.implicitly_wait(5)
username = driver.find_element_by_css_selector(".v-text-field__slot>input[type='text']").send_keys("20171404137")
password = driver.find_element_by_css_selector('.v-text-field__slot>input[type="password"]').send_keys("20171404137.")
js = "document.querySelector('.v-select__selections input').removeAttribute('readonly');"
driver.execute_script(js)
school = driver.find_element_by_css_selector('div.v-select__slot')
value = '山西省财政税务专科学校'
driver.execute_script("arguments[0].text=arguments[1];",school,value)
time.sleep(2)
login = driver.find_element_by_css_selector("span.v-btn__content").click()

# time.sleep(6)
# driver.quit()