# this is like the configuration file for all the py.tests
import pytest
from base.web_driver_factory import WebDriverFactory


@pytest.fixture()
def method_setup():
    print()
    print("Running method level setUp")
    yield
    print()
    print("Running method level tearDown")  # everything after yield runs after the test


# scope=module means it will run setUp before all the tests, and tearDown after all the tests
@pytest.fixture(scope="class")
def one_time_setup(request, browser, secret, remote):
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
    if browser == 'Firefox':
        cap = caps[1]
        print("Firefox")
    elif browser == 'Safari':
        cap = caps[2]
        print("Safari")
    else:
        print("Chrome")
    wdf = WebDriverFactory(browser, cap, secret, remote)
    driver = wdf.get_web_driver_instance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    if (remote == 'no'):
        print("TESTS EXECUTED LOCALLY")
    else:
        print("TESTS EXECUTED ON BROWSERSTACK")
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Tests matched!"}}')

    driver.quit()

    print("Running one time teardown")  # everything after yield runs after the test


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--dockerized")
    parser.addoption("--sec")
    parser.addoption("--remote")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def dockerized(request):
    return request.config.getoption("--dockerized")


@pytest.fixture(scope="session")
def secret(request):
    return request.config.getoption("--sec")


@pytest.fixture(scope="session")
def remote(request):
    return request.config.getoption("--remote")
