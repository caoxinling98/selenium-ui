from selenium import webdriver

driver = webdriver.Chrome('../../chromedriver.exe')
driver.get("https://www.baidu.com")
driver.implicitly_wait(5)
news = driver.find_element_by_name("tj_trnews").click()
driver.implicitly_wait(5)
driver.back()
driver.implicitly_wait(5)
driver.forward()
