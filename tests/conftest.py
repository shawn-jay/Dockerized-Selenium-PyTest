#this is like the configuration file for all the py.tests
import pytest
from base.webdriverfactory import WebDriverFactory

@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print()
    print("Running method level tearDown") #everything after yield runs after the test

@pytest.fixture(scope="class") #scope=module means it will run setUp before all the tests, and tearDown after all the tests
def oneTimeSetUp(request, browser):

    wdf = WebDriverFactory(browser)
    driver = wdf.get_web_driver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    #txt
    driver.quit()
    print("Running one time tearDown") #everything after yield runs after the test

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")