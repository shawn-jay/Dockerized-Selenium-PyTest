from pages.home.login_page import LoginPage
from utilities.test_status import RunStatus
import unittest
import pytest


@pytest.mark.usefixtures("one_time_setup", "method_setup")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, one_time_setup):
        self.lp = LoginPage(self.driver)
        # self.ts = TestStatus()

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("standard_user", "secret_sauce")
        result = self.lp.verify_login_successful()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("standard_user", "secret_sauce1")
        result = self.lp.verify_login_failed()
        assert result == True

    # @pytest.mark.run(order=3) # this should fail on purpose
    # def test_titleOfWebsite(self):
    #    result1 = self.lp.verify_title("Sauce Labs")
    #    self.ts.mark(result1, "Title is incorrect")
    #    #assert result1
    #    result2 = self.lp.verify_title("Swag Labs")
    #    self.ts.markFinal("test_VerifyTitle_2", result2, "Title 2 is incorrect")
    #    #assert result2
