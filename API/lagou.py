from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import traceback

driver = webdriver.Chrome("./chromedriver.exe")

try:
    driver.implicitly_wait(5)
    driver.get('https://www.lagou.com/zhaopin/Java/?labelWords=label')


    list_window = driver.current_window_handle
    driver.switch_to.window(list_window)

    # jobs_len = len(jobs)
    # i = 0

    while True:

        jobs = driver.find_elements_by_css_selector('.item_con_list li')

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.item_con_list li:first-child .p_top a span')
        ))

        for job in jobs:
            job_link = job.find_element_by_css_selector(
                '.p_top a span')
            # print(job_link, job_link.text)

            while True:
                try:
                    job_link.click()
                    WebDriverWait(driver, 3).until(EC.number_of_windows_to_be(2))

                    driver.switch_to.window(driver.window_handles[1])

                    company = driver.find_element_by_css_selector('.job-name .company')

                    job_name = driver.find_element_by_css_selector('.job-name .name')

                    salary = driver.find_element_by_css_selector('.job_request .salary')

                    spans = driver.find_elements_by_css_selector('.job_request p span')
                    work_age = spans[2]

                    print('公司：', company.text,
                          '; 职位名称：', job_name.text,
                          '; 薪资：', salary.text,
                          '; 工作经验：', work_age.text)
                except Exception as e1:
                    traceback.print_exc()
                    try:
                        time.sleep(5)
                        if driver.current_window_handle != list_window:
                            error = driver.find_element_by_css_selector('.i_error')
                            driver.close()
                            driver.switch_to.window(list_window)
                    except Exception as e2:
                        traceback.print_exc()
                        exit(1)
                    continue
                else:
                    driver.close()
                    driver.switch_to.window(list_window)
                break

        next_page = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.item_con_pager .pager_container > *:last-child')))
        # next_page = driver.find_element_by_css_selector('.item_con_pager .pager_container span:last-child')
        next_page_class = next_page.get_attribute('class')

        if 'pager_next_disabled' in next_page_class:
            break
        else:
            next_page.click()
            time.sleep(3)

except Exception as e:
    raise e
else:
    driver.quit()
finally:
    time.sleep(3)
    driver.quit()
