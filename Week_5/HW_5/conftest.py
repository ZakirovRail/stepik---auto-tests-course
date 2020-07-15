from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from datetime import datetime


# define  a command line options
def pytest_addoption(parser):
    parser.addoption('--type_browser', action='store', default="Chrome",
                     help="Choose browser: Chrome or Firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru, en, fr, es and etc.")


@pytest.fixture(scope="function")
def browser(request):
    type_browser = request.config.getoption("type_browser")
    user_language = request.config.getoption("language")
    browser = None
    if type_browser == "Chrome":
        print(f"\nstart Chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
    elif type_browser == "Firefox":
        print(f"\nstart {type_browser} browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.maximize_window()
    else:
        raise pytest.UsageError("--type_browser should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
