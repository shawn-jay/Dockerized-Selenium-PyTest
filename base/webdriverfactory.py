from selenium import webdriver


# Purpose fo this test case is to create a webdriver instance
# based on the Browser configurations
#
#

class WebDriverFactory():
    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):
        baseURL = "https://www.saucedemo.com/"
        driver = None
        print("Running one time setUp")
        if self.browser == 'firefox':
            driver = webdriver.Firefox()
            print("Running tests on FF")
        else:
            driver = webdriver.Chrome()
            print("Running tests on Chrome")

        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        return driver
