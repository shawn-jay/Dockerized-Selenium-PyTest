from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from threading import Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Purpose fo this test case is to create a webdriver instance
# based on the Browser configurations
#
#

class WebDriverFactory():

    def __init__(self, browser, cap_given, secret, remote):
        self.browser = browser
        self.cap_given = cap_given
        self.secret = secret
        self.remote = remote

    def get_web_driver_instance(self):
        desiredcap = self.cap_given
        baseURL = "https://www.saucedemo.com/"
        driver = None
        chrome_options = Options()
        chrome_options.add_argument('log-level=3')
        if self.remote != "no":
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
        print("Running one time setUp")
        if self.remote == 'no':
            driver = webdriver.Chrome(options=chrome_options)
        else:
            line = None
            with open('data.txt') as f:
                line = f.read()
            driver = webdriver.Remote(
                command_executor='https://shawnjafari2:' + line + '@hub-cloud.browserstack.com/wd/hub',
                desired_capabilities=desiredcap)
            print("Running tests on " + self.browser)

        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        return driver

