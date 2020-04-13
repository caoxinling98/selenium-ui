from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome("../../chromedriver.exe")
driver.get("https://www.baidu.com")
logo = driver.find_element_by_xpath("//div[@id='lg']/img[1]")
ac = ActionChains(driver)
ac.context_click(logo).send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(Keys.DOWN).perform()
# time.sleep(2)
# ac.send_keys(Keys.DOWN)
# time.sleep(2)
# ac.send_keys(Keys.DOWN)
# time.sleep(2)
# ac.send_keys(Keys.DOWN)
# time.sleep(2)
# ac.send_keys(Keys.DOWN)
# time.sleep(2)
# ac.send_keys(Keys.ENTER)
# ac.perform()
