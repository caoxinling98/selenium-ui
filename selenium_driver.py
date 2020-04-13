# coding=utf-8
from base.logger import Logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys


import time
import os.path
from conftest import IMG_DIR

# create a logger instance
logger = Logger(logger="BasePage").getlog()


class SeleniumDriver:

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        """
        def which generate locator type
        :param locator_type: str set by def which implement on SeleniumDriver class
        :return: tag type or False
        """
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'class':
            return By.CLASS_NAME
        elif locator_type == 'link':
            return By.LINK_TEXT
        elif locator_type == 'tag':
            return By.TAG_NAME
        else:
            logger.info("Locator type" + locator_type + " not correct/supported")
        return False

    def open(self, url):
        """
        open browser page
        :param project: str from fixture each_function_setup/one_time_setup
        :param path: str from page class ex LoginPage
        :return: None
        """
        self.driver.get(url)
        logger.info('Open page with url %s' % url)

    def element_get(self, locator, locator_type='id', web_element=None):
        """
        find element on dom tree of web page
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param web_element: WebElement returned by method ex element_get
        :return: WebElement
        """
        element = web_element
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            if element:
                element = web_element.find_element(by_type, locator)
                logger.info("Element descendant Found with locator: " + locator + " locator_type " + locator_type)
            else:
                element = self.driver.find_element(by_type, locator)
                logger.info("Element Found with locator: " + locator + " locator_type " + locator_type)
        except:
            logger.error("Element not found")
        return element

    def elements_get(self, locator, locator_type='id'):
        """
        find elements on dom tree of web page
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :return: WebElement array[]
        """
        elements = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            elements = self.driver.find_elements(by_type, locator)
            logger.info("Elements Found")
        except:
            logger.info("Elements not found")
        return elements

    def element_attribute(self, attr_name, locator='', locator_type='id', element=None):
        """
        find attribute value and return it
        :param attr_name: str from page class ex LoginPage
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param element: WebElement returned by method ex element_get
        :return: str attribute value
        """
        name = None
        if element is not None:
            try:
                name = element.get_attribute(attr_name)
                logger.info("Element Not Found with attribute %s" % attr_name)
            except:
                logger.info("Element Not Found with attribute %s" % attr_name)
        else:
            try:
                locator_type = locator_type.lower()
                by_type = self.get_by_type(locator_type)
                result = self.driver.find_element(by_type, locator)
                name = result.get_attribute(attr_name)
                logger.info("Elements Found")
            except:
                logger.info("Elements not found")
        return name

    def element_click(self, locator='', locator_type='id', web_element=None):
        """
        click on element
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param web_element: WebElement returned by method ex element_get
        :return:
        """
        try:
            if web_element:
                web_element.click()
                logger.info("Clicked on element")
            else:
                element = self.element_get(locator, locator_type)
                element.click()
                logger.info("Clicked on element with locator: " + locator + " locator_type: " + locator_type)
        except:
            logger.info("Cannot click on the element with locator: " + locator + " locator_type: " + locator_type)

    def element_send_keys(self, locator, data, locator_type='id', element=None):
        """
        Send keys to field
        :param locator: str from page class ex LoginPage
        :param data: value which send
        :param locator_type: str from page class ex LoginPage
        :param element: WebElement returned by method ex element_get
        :return:
        """
        try:
            if element is not None:
                element.send_keys(data)
            else:
                element = self.element_get(locator, locator_type)
                element.send_keys(data)
            logger.info("Send data on element with locator: " + locator + " locator_type: " + locator_type)
        except:
            logger.info("Cannot send data on the element with locator: " + locator + " locator_type: " + locator_type)

    def element_is_present(self, locator, locator_type='id'):
        """
        verify is element present on dom at web page
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :return: bool
        """
        try:
            element = self.element_get(locator, locator_type)
            if element is not None:
                return True
            else:
                logger.info("Element not found")
                return False
        except:
            logger.info("Element not found")
            return False

    def element_presence_check(self, locator, locator_type='id'):
        """
        verify is element present at web page
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :return: bool
        """
        try:
            elementList = self.elements_get(locator, locator_type)
            if len(elementList) > 0:
                logger.info("Element not found")
                return True
            else:
                logger.info("Element not found")
                return False
        except:
            logger.info("Element not found")
            return False

    def element_wait_for(self, locator, locator_type='id', timeout=10, poll_frequency=0.5):
        """
        wait while element to be available for click
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param timeout: int timeout
        :param poll_frequency: int query per second to element
        :return: WebElement
        """
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            logger.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            logger.info("Element appeared on the web page")
        except:
            logger.info("Element not appeared on the web page")
        return element

    def element_visibility_wait_for(self, locator, locator_type='id', timeout=10, poll_frequency=0.5):
        """
        wait while element to be visible
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param timeout: int timeout
        :param poll_frequency: int query per second to element
        :return: WebElement
        """
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            logger.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((by_type, locator)))
            logger.info("Element appeared on the web page")
        except:
            logger.info("Element not appeared on the web page")
        return element

    def element_is_displayed(self, locator="", locator_type="id", element=None):
        """
        Check element is displayed and not hidden by another element
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param element: WebElement returned by method ex element_get
        :return: bool
        """
        is_displayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.element_get(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                logger.info("Element is displayed")
            else:
                logger.info("Element not displayed")
            return is_displayed
        except:
            print("Element not found")
            return False

    def element_is_clickable(self, locator, locator_type='id', timeout=20, poll_frequency=0.5):
        """
        Check element is available for click
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param timeout: int timeout
        :param poll_frequency: int query per second to element
        :return: WebElement
        """
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            logger.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException,
                                                     ElementClickInterceptedException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            logger.info("Element is ready for click")
        except:
            logger.info("Element is not clickable")
        return element

    def element_get_text(self, locator="", locator_type="", element=None, info=""):
        """
        Return element text
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param element: WebElement returned by method ex element_get
        :param info:
        :return: str
        """
        try:
            if locator:
                element = self.element_get(locator, locator_type)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute('InnerText')
            if len(text) != 0:
                logger.info("Getting text on element :: " + info)
                logger.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            logger.error("Failed to get text on element " + info)
            text = None
        return text

    def get_url(self):
        """
        Get current page url
        :return: str
        """
        current_url = None
        try:
            current_url = self.driver.current_url
            logger.info('Current URL is :: ' + current_url)
        except:
            logger.error('Failed to get current URL ' + current_url)
        return current_url

    def get_title(self):
        """
        Get current page elemen with class 'Title'
        :return: WebElement
        """
        title = None
        try:
            title = self.driver.title
            logger.info('Current title is :: ' + title)
        except:
            logger.error('Failed to get title ' + title)
        return title

    def open_new_tab(self, locator="", locator_type="id", timeout=10):
        """
        Open new tab
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param timeout: int timeout
        :return: int open tabs count
        """
        handles_before = self.driver.window_handles
        self.element_click(locator=locator, locator_type=locator_type)
        handles_after = None
        try:
            WebDriverWait(self, timeout).until(lambda windows: len(handles_before) != len(self.driver.window_handles))
            handles_after = self.driver.window_handles
            logger.info('New window is opened :: ' + self.get_title())
            return handles_after
        except:
            logger.error('No new window opened')
        return handles_after

    def switch_window(self, window_number):
        """
        Switch to another tab
        :param window_number: int window tab number
        :return: bool
        """
        try:
            self.driver.switch_to_window(self.driver.window_handles[window_number])
            logger.info('Switched on new windows :: ' + self.get_title())
            return True
        except:
            logger.error('Can`t switched to the window :: ' + str(window_number))
            return False

    def element_clear(self, locator, locator_type='id'):
        """
        Clear element field
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :return: None
        """
        try:
            element = self.element_get(locator, locator_type)
            element.clear()
            logger.info("Cleared on element with locator: " + locator + " locator_type: " + locator_type)
        except:
            logger.info("Cannot clear on the element with locator: " + locator + " locator_type: " + locator_type)

    def element_clear_by_keys(self, locator, locator_type='id', attribute='value'):
        """
        Clear field with sending Keys_BACKSPACE to field
        :param locator: str from page class ex LoginPage
        :param locator_type: str from page class ex LoginPage
        :param attribute: attribute by which determines how much keys sending
        :return: None
        """
        try:
            element = self.element_get(locator, locator_type)
            value = element.get_attribute(attribute)
            for i in range(len(value)):
                element.send_keys(Keys.BACKSPACE)
            logger.info("Cleared on element with locator: " + locator + " locator_type: " + locator_type)
        except:
            logger.info("Cannot clear on the element with locator: " + locator + " locator_type: " + locator_type)


    def get_windows_img(self):

        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = IMG_DIR + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshots and save to folder : /screenshots")
        except Exception as e:
            self.get_windows_img()
            logger.error("Failed to take screenshots! %s" % e)