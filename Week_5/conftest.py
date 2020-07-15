from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from datetime import datetime


# define  a command line options
def pytest_addoption(parser):
    parser.addoption('--type_browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru, en, fr, es and etc.")


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
        browser.maximize_window()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
        browser.maximize_window()
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
    browser.save_screenshot('Screenshots/screenshot-%s.png' % now)
    browser.quit()


# My original version of fixture
# @pytest.fixture(scope="function")
# def browser(request):
#     type_browser = request.config.getoption("type_browser")
#     user_language = request.config.getoption("language")
#     browser = None
#     if type_browser == "chrome":
#         print(f"\nstart chrome browser for test..")
#         options = Options()
#         options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#         browser = webdriver.Chrome(options=options)
#     elif type_browser == "firefox":
#         print(f"\nstart {type_browser} browser for test..")
#         fp = webdriver.FirefoxProfile()
#         fp.set_preference("intl.accept_languages", user_language)
#         browser = webdriver.Firefox(firefox_profile=fp)
#     else:
#         raise pytest.UsageError("--type_browser should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
