from selenium import webdriver
import time
def my_refresh(target_url,refresh_count):
    driver = webdriver.Chrome()
    driver.get(target_url)
    time.sleep(2)
    for i in  range(refresh_count):
        driver.refresh()
        time.sleep(1)
    else:
        print('刷新完毕')
        print(i)

my_refresh("https://www.baidu.com",5)