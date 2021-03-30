from pages.home.login_page import LoginPage
from utilities.test_status import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus()

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("standard_user", "secret_sauce")
        result = self.lp.verifyLoginSuccessful()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("standard_user", "secret_sauce1")
        result = self.lp.verifyLoginFailed()
        assert result == True

    @pytest.mark.run(order=3) # this should fail on purpose
    def test_titleOfWebsite(self):
        result1 = self.lp.verifyTitle("Sauce Labs")
        self.ts.mark(result1, "Title is incorrect")
        #assert result1
        result2 = self.lp.verifyTitle("Swag Labs")
        self.ts.markFinal("test_VerifyTitle_2", result2, "Title 2 is incorrect")
        #assert result2