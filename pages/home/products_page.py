from base.selenium_driver import SeleniumDriver
import time


class ProductPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _filter_sort = 'product_sort_container'

    def filter_by_visible_text(self, option_name):
        self.select_option(self._filter_sort, option_name, "class")



