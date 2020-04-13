#杜易学
from selenium import webdriver
from time import sleep

browser = webdriver.Chrome("../../chromedriver.exe")
browser.get("https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95?labelWords=&fromSearch=true&suginput=")

flag = False
# browser.maximize_window()

while not flag:
    # 获取当前页面的公司名称
    company_name_list = browser.find_elements_by_css_selector('.company_name')
    # 獲取当前页面的测试岗位
    job_list = browser.find_elements_by_css_selector('.position_link>h3')
    # 获取地理位置
    address_listv = browser.find_elements_by_css_selector('.add>em')
    # 发布时间
    out_time = browser.find_elements_by_css_selector('.format-time')
    # 薪资待遇
    salary_list = browser.find_elements_by_css_selector('.money')
    # 经验
    # experience_list = browser.find_elements_by_xpath('//*[@id="s_position_list"]/ul[8]/div[1]/div[1]/div[2]/div/text()')
    print('----------当前页------------------')
    for i in range(len(company_name_list)):
        print("公司：", company_name_list[i].text, "地点：", address_listv[i].text, '发布时间：' + out_time[i].text,
              "岗位：" + job_list[i].text, "待遇：", salary_list[i].text)
    try:
        # next_page = browser.find_element_by_xpath(".//*[@id='s_position_list']/div[2]/div/span[6]")
        next_page = browser.find_element_by_css_selector(".pager_next")
        browser.execute_script("arguments[0].click();", next_page)
        sleep(2)
    except:
        if 'login.html' in browser.current_url:
            print("请登录")
        else:
            print("异常")
        flag = True
