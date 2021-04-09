import time
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
from selenium.webdriver.support.ui import Select
import logging


class SeleniumDriver:

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def _get_by_type(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def get_element(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self._get_by_type(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.info("Element not found")
        return element

    def element_click(self, locator, locatorType="id"):
        try:
            element = self.get_element(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack()

    def send_keys(self, data, locator, locatorType="id"):
        try:
            element = self.get_element(locator, locatorType)
            element.send_keys(data)
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator + " locatorType: " + locatorType)
            print_stack() #it will show the error and will help where the error occured. Useful in debugging

    def is_element_present(self, locator, locatorType="id"):
        try:
            element = self.get_element(locator, locatorType)
            if element is not None:
                self.log.info("Element Found with locator: " + locator + " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not found with locator: " + locator + " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def check_for_element(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def wait_for_element(self, locator, locatorType="id",
                         timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self._get_by_type(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            #WebDriverWait is an explicit wait that waits for a certain condition
            #to occur before proceeding further in the code
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def select_option(self, locator, option_name, locatorType='class'):
        selectButton = Select(self.get_element(locator, locatorType))

        selectButton.select_by_visible_text(str(option_name))
        time.sleep(3)

    def get_attribute(self, locator, locatorType, attribute):
        item = self.get_element(locator, locatorType)
        val = item.get_attribute(attribute)
        self.log.info(str(val))
        print(str(val))