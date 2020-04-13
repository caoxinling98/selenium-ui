import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class TestBaiduSearch():

    @pytest.mark.usefixtures('login')
    def test_search(self,login):
        login.get('https://www.baidu.com')
        ele = login.find_element_by_id('kw')
        ele.send_keys('selenium'+Keys.ENTER)
        time.sleep(10)

