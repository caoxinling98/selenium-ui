import allure
from pages.home_page import HomePage
import time

class TestBaiduSearch():

    @allure.feature('用户功能')

    @allure.story('百度搜索')
    def test_baidu_search(self,login,base_url):
        page = HomePage(login)
        page.open(base_url)
        page.enter_search('pytest')
        page.click_search_button()
        time.sleep(10)
