from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("../../chromedriver.exe")
driver.get("file:///D:/python/selenium_pages-master/form_web_element.html")
select_teacher =  Select(driver.find_element_by_id("ss_multi"))
select_teacher.deselect_all()
select_teacher.select_by_visible_text("小雷老师")
