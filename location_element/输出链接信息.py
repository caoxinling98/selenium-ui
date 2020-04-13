from selenium import webdriver

driver=webdriver.Chrome("../../chromedriver.exe")
driver.get("https://www.baidu.com")
elements=driver.find_elements_by_tag_name("a")
for element in elements:
    print(element.text)