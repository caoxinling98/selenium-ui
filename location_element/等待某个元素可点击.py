from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome('../../chromedriver')
driver.get("https://www.baidu.com")
try:
    click1 = WebDriverWait(driver,5).until(
        ec.element_to_be_clickable((By.NAME,'tj_trnews'))
    )
    click1.click()
    print(driver.title)
except Exception as e:
    print(e)
finally:
    print("hello")