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

    wdf = WebDriverFactory(browser, secret, remote)
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
