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
    def click_login_link(self):
        self.element_click(self._login_link, locatorType="link")

    def enter_email(self, email):
        self.log.info("testing inheritance")
        self.send_keys(email, self._email_field)

    def enter_password(self, password):
        self.send_keys(password, self._password_field)

    def click_login_button(self):
        self.element_click(self._login_button, locatorType="class")

    def login(self, email="", password=""):
        #self.clickLoginLink()
        self.driver.refresh()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(2)

    def verify_login_successful(self):
        result = self.is_element_present("//div[contains(text(), 'Labs Backpack')]", "xpath")
        return result

    def verify_login_failed(self):
        result = self.is_element_present("//h3[@data-test='error']", "xpath")
        return result

    def verify_title(self, title):
        if self.get_title() == title:
            return True
        else:
            self.log.info(str(self.get_title()))
            return False
