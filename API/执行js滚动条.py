from selenium import webdriver
import time

driver = webdriver.Chrome('../../chromedriver.exe')
driver.get("https://tieba.baidu.com")
driver.maximize_window()
time.sleep(5)
# js="window.scrollTo(0,document.body.scrollHeight)"
# js1="window.scrollTo(document.body.scrollHeight,0)"
# driver.execute_script(js)
# time.sleep(2)
# driver.execute_script(js1)
target = driver.find_element_by_xpath('//*[@id="f-d-w"]/div[12]')
print(target.text)
driver.execute_script("arguments[0].scrollIntoView();",target)