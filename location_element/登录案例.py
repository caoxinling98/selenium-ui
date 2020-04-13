from selenium import webdriver
# 显示等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome('../../chromedriver.exe')
driver.get("https://github.com/login")
username = driver.find_element_by_xpath('//input[@id="login_field"]').send_keys("caoxinling98")
passwd = driver.find_element_by_xpath('//input[@id="password"]').send_keys("caoxinling123.")
submit=driver.find_element_by_xpath("//input[@name='commit']")
submit.click()
ele = WebDriverWait(driver,5).until(
    ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/header/div[7]/details/summary/span[2]'))
)
ele.click()
username1 = driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/details-menu/div[1]/a/strong")
print(username1.text)
if username1.text == "caoxinling98":
    print("与登录用户名一致")
else:
    print("与登录用户名不一致")