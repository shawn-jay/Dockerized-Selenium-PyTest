from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Purpose fo this test case is to create a webdriver instance
# based on the Browser configurations
#
#

class WebDriverFactory():
    def __init__(self, browser):
        self.browser = browser

    def get_web_driver_instance(self):
        baseURL = "https://www.saucedemo.com/"
        driver = None
        chrome_options = Options()
        dockerized = "True"
        if(dockerized == "True"):
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
        print("Running one time setUp")
        if self.browser == 'firefox':
            driver = webdriver.Firefox()
            print("Running tests on FF")
        else:
            driver = webdriver.Chrome(options=chrome_options)
            print("Running tests on Chrome")

        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        return driver
