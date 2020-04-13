from selenium import webdriver

driver = webdriver.Chrome('D:\python\chromedriver.exe')
driver.get("file:///D:/python/selenium_pages-master/iframe_sample.html")
driver.switch_to.frame("innerFrame")
vegetables = driver.find_elements_by_class_name("plant")
for vegetable in vegetables:
    print(vegetable.text)

driver.close()