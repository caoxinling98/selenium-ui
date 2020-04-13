from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("../../chromedriver.exe")
try:
    driver.implicitly_wait(5)
    driver.get("https://www.lagou.com/zhaopin/Java/?labelWords=label")
    driver.find_element_by_css_selector(".body-btn").click()

    window_list = driver.current_window_handle
    driver.switch_to.window(window_list)

    while True:
        jobs = driver.find_elements_by_css_selector('.item_con_list li')

        for job in jobs:
            job_link = job.find_element_by_css_selector('.p_top a span')
            job_link.click()

            driver.switch_to.window(driver.window_handles[1])

            job_company = driver.find_element_by_css_selector('.company')
            job_name = driver.find_element_by_css_selector('.name')
            job_money = driver.find_element_by_css_selector('.salary')

            print('公司：',job_company.text,
                  '职位名称：',job_name.text,
                  '薪资范围：',job_money.text)
            driver.close()
            driver.switch_to.window(window_list)

        next_page = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.item_con_pager .pager_container > *:last-child')))
        # next_page = driver.find_element_by_css_selector('.item_con_pager .pager_container span:last-child')
        next_page_class = next_page.get_attribute('class')

        if 'pager_next_disabled' in next_page_class:
            break
        else:
            next_page.click()
            time.sleep(3)

finally:
    time.sleep(10)
    driver.quit()