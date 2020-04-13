from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome("../../chromedriver.exe")
driver.get("https://v3.alphacoding.cn/login")
logo=driver.find_element_by_css_selector("html body div#__nuxt div#__layout div#app.v-application.v-application--is-ltr.theme--light div.v-application--wrap div.alphacoding-login header.login-navbar.v-sheet.v-sheet--tile.theme--light.v-toolbar.v-app-bar.v-app-bar--fixed div.v-toolbar__content div.v-toolbar__title.alphacoding-logo a img")
if logo.is_enabled():
    print("logo可用")
name=driver.find_element_by_xpath("//input[@id='input-13']")
passwd=driver.find_element_by_xpath("//input[@id='input-14']")
if name.is_enabled() and passwd.is_enabled():
    print("账号和密码框可用")
xiala=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[1]/div[4]/div[2]/div/div/div[1]/div[2]/div/i")
if xiala.is_enabled():
    print("下拉框可用")
select=xiala.click()
options=driver.find_elements_by_xpath("//div[@role='option']")
for option in options:
    print(option.text)
print(len(options))
if len(options) == '36':
    print("长度符合:")
submit = driver.find_element_by_xpath("//*[@id='app']/div/div/div[1]/div[5]/button")
if submit.is_enabled():
    print("登录按钮可用")
