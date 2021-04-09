from pages.home.login_page import LoginPage
from utilities.test_status import RunStatus
import unittest
import pytest


@pytest.mark.usefixtures("one_time_setup", "method_setup")
class LoginTests2(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, one_time_setup):
        self.lp = LoginPage(self.driver)
        # self.ts = TestStatus()

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.lp.login("standard_user", "secret_sauce")
        result = self.lp.verify_login_successful()
        assert result == True
