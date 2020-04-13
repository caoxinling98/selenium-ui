# 完整版
from selenium import webdriver
import time
driver = webdriver.Chrome("../../chromedriver.exe")
driver.get("https://book.douban.com/")
#豆瓣书店
book_shop = driver.find_element_by_xpath("//div[@class='nav-items']/ul/li[3]").click()
driver.switch_to.window(driver.window_handles[0])
print("******************第1页********************")
i = 2
while True:
    time.sleep(5)
    # 获取书名
    list1 =  driver.find_elements_by_xpath("//h3")
    for book_name in list1:
        print(book_name.text)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    try:
        # 下一页
        next_page = driver.find_element_by_xpath("//a[text()='后页»']")
        driver.execute_script("arguments[0].click();",next_page)
    except Exception as e:
        print(e)
    finally:
        print("******************第" + str(i) + "页********************")
    i += 1
    if not(next_page.is_displayed()):
        break
