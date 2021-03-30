from pages.home.login_page import LoginPage
from utilities.test_status import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests2(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus()

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("standard_user", "secret_sauce")
        result = self.lp.verifyLoginSuccessful()
        assert result == True