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
    caps = [{
        'os_version': '10',
        'os': 'Windows',
        'browser': 'chrome',
        'browser_version': '89.0',
        'name': 'Parallel Test1',  # test name
        'build': 'browserstack-build-1'  # Your tests will be organized within this build
    },
    {
        'os_version': '10',
        'os': 'Windows',
        'browser': 'firefox',
        'browser_version': 'latest',
        'name': 'Parallel Test2',
        'build': 'browserstack-build-1'
    },
    {
        'os_version': 'Big Sur',
        'os': 'OS X',
        'browser': 'safari',
        'browser_version': 'latest',
        'name': 'Parallel Test3',
        'build': 'browserstack-build-1'
    }]

    cap = caps[0]
    if browser == 'Firefox':
        cap = caps[1]
        print("Firefox")
    elif browser == 'Safari':
        cap = caps[2]
        print("Safari")
    else:
        print("Chrome")
    wdf = WebDriverFactory(browser, cap)
    driver = wdf.get_web_driver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    #txt
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Tests matched!"}}')
    driver.quit()

    print("Running one time tearDown") #everything after yield runs after the test

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")
    parser.addoption("--dockerized")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

@pytest.fixture(scope="session")
def dockerized(request):
    return request.config.getoption("--dockerized")