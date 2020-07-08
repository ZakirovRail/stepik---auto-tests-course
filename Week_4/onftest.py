# import pytest
# from selenium import webdriver
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

#=======================================================================================================================

import pytest
from selenium import webdriver

#In case if we WANT to cpecify a type of browser in command line - default=None
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")

#In case if don't want to cpecify a type of browser in command line - default="chrome"
# parser.addoption('--browser_name', action='store', default="chrome",
#                  help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
