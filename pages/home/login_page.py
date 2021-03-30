from base.selenium_driver import SeleniumDriver
import time


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user-name"
    _password_field = "password"
    _login_button = "btn_action"

    #action methods
    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.log.info("testing inheritance")
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="class")

    def login(self, email="", password=""):
        #self.clickLoginLink()
        self.driver.refresh()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(2)

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//div[contains(text(), 'Labs Backpack')]", "xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//h3[@data-test='error']", "xpath")
        return result

    def verifyTitle(self, title):
        if self.getTitle() == title:
            return True
        else:
            self.log.info(str(self.getTitle()))
            return False
