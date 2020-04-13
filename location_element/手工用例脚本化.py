from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
str1=driver.find_element_by_id('kw').send_keys("selenium")
button=driver.find_element_by_id('su').click()
time.sleep(3)
# 竞价排名
guangao=driver.find_elements_by_xpath('//*[@id="4001"]/div[3]/font[2]/a/span')
lenn=str(len(guangao))
print(lenn)
for a in guangao:
    print(a.text)
# 竞价排名后的第一个链接是否为官网
first=driver.find_element_by_xpath('//div[@id='+lenn+']/h3/a').get_attribute('text')
print(first)
if  (first == "Selenium automates browsers. That's it!"):
    print("竞价排名后的第一个链接是selenium官网")
else:
    print('不是')
