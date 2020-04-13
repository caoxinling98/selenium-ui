from selenium import webdriver
import re

dir=webdriver.Chrome("../../chromedriver.exe")
dir.get("http://home.baidu.com/contact.html")

str1=dir.page_source
emails=re.findall(r'[\w]{0,19}@baidu.com',str1)
for email in emails:
    print(email)