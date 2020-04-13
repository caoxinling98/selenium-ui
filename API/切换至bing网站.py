from selenium import webdriver

driver = webdriver.Chrome('../../chromedriver.exe')
driver.get("file:///D:/python/selenium_pages-master/swtich_window_sample.html")
mainWindow = driver.current_window_handle
a = driver.find_element_by_tag_name("a")
a.click()
driver.switch_to.window(driver.window_handles[1])
print(driver.title)

driver.close()