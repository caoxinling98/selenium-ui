from selenium import webdriver

driver = webdriver.Chrome("../../chromedriver.exe")
driver.get("https://www.baidu.com")
content = driver.find_element_by_id("kw").send_keys("selenium")
submit = driver.find_element_by_id("su").click()
driver.implicitly_wait(2)
text1 = driver.find_element_by_xpath("//div[@id=1]")
print(text1.text)