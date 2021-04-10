from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium import webdriver


# Purpose of this class is to create a webdriver instance. The fully initialized driver will be returned
# based on the Browser configurations
#
#

class WebDriverFactory():

    def __init__(self, browser, secret, remote):
        self.browser = browser
        self.secret = secret
        self.remote = remote

    def get_web_driver_instance(self):
        caps = [{
            'os_version': '10',
            'os': 'Windows',
            'browser': 'chrome',
            'browser_version': '89.0',
            'name': 'Chrome Test 1',  # test name
            'build': 'browserstack-build-1'  # Your tests will be organized within this build
        },
        {
            'os_version': '10',
            'os': 'Windows',
            'browser': 'firefox',
            'browser_version': 'latest',
            'name': 'Firefox Test 1',
            'build': 'browserstack-build-1'
        },
        {
            'os_version': 'Big Sur',
            'os': 'OS X',
            'browser': 'safari',
            'browser_version': 'latest',
            'name': 'Safari Test 1',
            'build': 'browserstack-build-1'
        }]

        cap = caps[0]  # default use Chrome
        if self.browser == 'Firefox':
            cap = caps[1]
            print("Firefox")
        elif self.browser == 'Safari':
            cap = caps[2]
            print("Safari")
        else:
            print("Chrome")

        desiredcap = cap
        baseURL = "https://www.saucedemo.com/"
        driver = None
        chrome_options = Options()
        chrome_options.add_argument('log-level=3')
        # Below code is used if you're running a test on a Docker container
        #if self.remote != "no":
        #    chrome_options.add_argument("--headless")
        #    chrome_options.add_argument("--no-sandbox")
        #    chrome_options.add_argument("--disable-dev-shm-usage")
        print("Running one time setUp")
        if self.remote == 'no':
            driver = webdriver.Chrome(options=chrome_options)
        else:
            try:
                with open('data.txt') as f:
                    line = f.read()
            except OSError as e:
                print(str(e))

            driver = webdriver.Remote(
                command_executor='https://shawnjafari2:' + line + '@hub-cloud.browserstack.com/wd/hub',
                desired_capabilities=desiredcap)
            print("Running tests on " + self.browser)

        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        return driver

