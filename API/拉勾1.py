from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('../../chromedriver.exe')
# driver.get("https://www.lagou.com/")
# search_input = driver.find_element_by_id("search_input").send_keys('java')
# search_button = driver.find_element_by_xpath("//input[@value='搜索']")
driver.get("https://www.lagou.com/jobs/list_web%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95/p-city_2?px=default&gj=%E4%B8%8D%E8%A6%81%E6%B1%82&xl=%E5%A4%A7%E4%B8%93#filterBox")
mainWindow = driver.current_window_handle
# 关闭弹窗广告
driver.find_element_by_xpath("/html/body/div[9]/div/div[2]").click()
#页数
i = 2
print("----------------------第1页开始----------------------")
while True:
    time.sleep(3)
    # 获得每页职位
    list1 = driver.find_elements_by_xpath("//h3")
    for a in list1:
        #点击每个职位
        driver.execute_script("arguments[0].click();", a)
        #跳转到详情页
        driver.switch_to.window(driver.window_handles[1])
        # 获取信息
        position_name = driver.find_element_by_xpath("//h1[@class='name']").text
        company_name = driver.find_element_by_xpath("//h4[@class='company']").text
        salary = driver.find_element_by_xpath("//span[@class='salary']").text
        jingyan = driver.find_element_by_xpath("//dd[@class='job_request']/h3/span[3]").text
        print("公司：",company_name,"；职位名称：",position_name,"；薪资：",salary,"；工作经验：",jingyan)
        driver.close()
        #回到主页
        driver.switch_to.window(driver.window_handles[0])
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    # if 'pager_next_disabled' in next_page.get_att
    try:
        # i1 = str(i)
        #点击下一页
        next_page = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR,'.item_con_pager .pager_container > *:last-child')))
        driver.execute_script("arguments[0].click();", next_page)
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print(e)
    finally:
        print("----------------------第"+str(i)+"页开始----------------------")
    i += 1