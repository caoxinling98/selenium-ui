from base.logger import Logger
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as ec
from conftest import IMG_DIR

#logger实例
logger = Logger(logger="BasePage").getlog()

class BasePage(object):

    def __init__(self,login):
        """
        :param login:conftest.py的login
        """
        self.driver = login

    #后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")


    def forward(self):
        self.driver.forward()
        logger.info('Click forward on current page.')

    def open(self,url):
        self.driver.get(url)
        logger.info("Open page with url:%s"%url)

    def get_url(self):
        current_url = None
        try:
            current_url = self.driver.current_url
            logger.info('Current UFL is ::'+ current_url)
        except:
            logger.error('Failed get current url ::'+current_url)
        return current_url

    def get_title(self):
        title = None
        try:
            title = self.driver.title
            logger.info('Current title is ::'+ title)
        except:
            logger.error('Failed get current title ::'+title)
        return title

    def open_new_tab(self,locator='' , locator_type='id', timeout=10):

        handles_before = self.driver.window_handles
        self.element_click(locator=locator,locator_type=locator_type)
        handles_after = None
        try:
            WebDriverWait(self.driver,timeout).until(lambda windows:len(handles_before) != len(self.driver.window_handles))
            handles_after = self.driver.window_handles
            logger.info('New window is opened ::' + self.get_title())
            return handles_after
        except:
            logger.error('NO new window opened')
        return handles_after

    def switch_window(self,window_number):
        try:
            self.driver.switch_window(self.driver.window_handles[window_number])
            logger.info('Switched on new window::' + self.get_title())
            return True
        except:
            logger.error('Failed to switch on new window::'+self.get_title())
            return False

    def get_by_type(self,locator_type):

        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'class':
            return By.CLASS_NAME
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'link':
            return By.LINK_TEXT
        elif locator_type == 'tag':
            return By.TAG_NAME
        else:
            logger.info("Locator_type：" + locator_type + " not correct")
        return False
    #定位元素
    def element_get(self,locator,locator_type = 'id',web_element=None):
    #locator相当于‘su’
        element = web_element
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            if element:
                element = web_element.find_element(by_type,locator)
                logger.info('Element descendant Found with locator：' + locator + "，locator_type：" + locator_type)
            else:
                element = self.driver.find_element(by_type,locator)
                logger.info('Element Found with locator：'+locator+'，locator_type：'+locator_type)
        except:
            logger.error('element not found')
        return element

    def elements_get(self,locator , locator_type='id'):
        elements = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            elements = self.driver.find_elements(by_type,locator)
            logger.info('Elements found')
        except:
            logger.error('Elements not found')
        return elements

    def element_click(self,locator='',locator_type='id',web_element=None):
        try:
            if web_element:
                web_element.click()
                logger.info('Clicked on element')

            else:
                element = self.element_get(locator,locator_type)
                element.click()
                logger.info('Clicked on element with locator：'+locator+'，locator_type：'+locator_type)
        except:
            logger.error('Cannot click on the element with locator：'+locator+'，locator_type：'+locator_type)

    def element_send_keys(self,locator,data,locator_type='id',web_element=None):
        try:
            if web_element:
                web_element.send_keys(data)
                logger.info('输入值成功！')
            else:
                element = self.element_get(locator,locator_type)
                element.send_keys(data)
            logger.info('send data：“'+data+'”on element with locator：'+locator+'，locator_type：'+locator_type)
        except Exception as e:
            logger.error('Cannot send content：“'+data+'” on element with locator：'+locator+'，locator_type：'+locator_type)
            print(e)

    def element_attribute(self,attr_name,locator='',locator_type='id',element=None):
        name = None
        if element:
            try:
                name = element.get_attribute(attr_name)
                logger.info('Element found with attribute %s'%attr_name)
            except:
                logger.error('Element not found with attribute %s'%attr_name)
        else:
            try:
                locator_type = locator_type.lower()
                by_type = self.get_by_type(locator_type)
                name = self.driver.find_element(by_type,locator).get_attribute(attr_name)
                logger.info('Element found with attribute %s'%attr_name)
            except:
                logger.error('Element not found with attribute %s' % attr_name)
        return name

    def element_is_parsent(self,locator,locator_type='id'):
        try:
            element = self.elements_get(locator,locator_type)
            if element:
                logger.info('Element found')
                return True
            else:
                logger.error('Element not found')
                return False
        except:
            logger.error('Element not found')
            return False

    def element_parsence_check(self,locator,locator_type='id'):
        try:
            elementList = self.elements_get(logger,locator_type)
            if (len(elementList)) > 0:
                logger.info('Element found')
                return True
            else:
                logger.error('Element not found')
                return False
        except:
            logger.error('Element not found')
            return False

    def element_wait_for(self,locator,locator_type='id',timeout=10,poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            logger.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll_frequency,ignored_exceptions=[NoSuchElementException,
                                                                                                               ElementNotVisibleException,
                                                                                                               ElementNotSelectableException])
            element = wait.until(ec.visibility_of_element_located((by_type,logger)))
            logger.info('Element appeared on the web page')
        except:
            logger.error('Element not appeared on the web page')
        return element

    def element_is_displayed(self,locator ='' ,locator_type='id',element=None):
        is_displayed = False
        try:
            if locator:
                element = self.elements_get(locator,locator_type)
            if element:
                is_displayed = element.is_displayed()
                logger.info('Element is displayed')
            else:
                logger.error('Element is not displayed')
            return is_displayed
        except:
            logger.error('Element is not displayed')
            return False

    def element_is_clickable(self,locator , locator_type='id',timeout=10,poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            logger.info('Waiting for maximum::'+ str(timeout)+ '::seconds for element to be clickable')
            wait = WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotSelectableException,
                                                     ElementNotVisibleException,
                                                     ElementClickInterceptedException])
            element = wait.until(ec.element_to_be_clickable((by_type,locator)))
            logger.info('Element is ready for click')
        except:
            logger.error('Element is clickable')
        return element

    def element_get_text(self , locator='',locator_type='',element = None , info=""):
        try:
            if locator:
                element = self.element_get(locator,locator_type)
            text = element.text
            if (len(text)) == 0:
                text = element.get_attribute('innerText')
            else:
                logger.info('Getting text on element::'+info)
                logger.info('The text is ::“'+text+'”')
                text = text.strip()
        except:
            logger.error('Failed to get text on element '+ info)
            text = None
        return text

    def element_clear(self,locator,locator_type='id'):
        try:
            element = self.element_get(locator,locator_type)
            element.clear()
            logger.info('Cleared on element with locator: '+locator+',locator_type: '+locator_type)
        except:
            logger.error('Cannot cleared on element with locator: '+locator+',locator_type: '+locator_type)

    def element_clear_by_keys(self,locator,locator_type='id',attribute='value'):
        try:
            element = self.element_get(locator,locator_type)
            value = element.get_attribute(attribute)
            for i in range(len(value)):
                element.send_keys(Keys.BACKSPACE)
            logger.info('Cleared on element with locator: '+locator+',locator_type: '+locator_type)
        except:
            logger.error("Cannot clear on the element with locator: " + locator + " locator_type: " + locator_type)

    def get_windows_img(self):

        creat_time = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name = IMG_DIR+creat_time+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshots and save to folder : /screenshots")
        except Exception as e:
            logger.error("Failed to take screenshots! %s"%e)
