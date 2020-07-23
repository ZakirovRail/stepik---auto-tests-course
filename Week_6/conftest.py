from selenium import webdriver
from logging import getLogger
import pytest
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from Week_6.constants import IMPLICIT_WAIT, WINDOWS_SIZE
from faker import Faker

# define  a command line options
def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en", help="Choose interface language:en, ru.")


logger = getLogger(__name__)


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("browser")
    user_language = request.config.getoption('language')
    if browser.lower() == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_language': user_language})
        driver = webdriver.Chrome(options=options)
        print("\nstart chrome browser for test..")
        # browser.maximize_window() # if we uncomment this line we comment the line with driver.set_window_size(*WINDOWS_SIZE)
    elif browser.lower() == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(firefox_profile=fp)
        print("\nstart firefox browser for test..")
        # browser.maximize_window() # if we uncomment this line we comment the line with driver.set_window_size(*WINDOWS_SIZE)
    else:
        print("Browser {} still is not implemented".format(browser))
    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.set_window_size(*WINDOWS_SIZE)
    yield driver
    print("\nquit browser..")
    # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
    driver.save_screenshot('Screenshots/screenshot-%s.png' % now)
    driver.quit()


# it's an example, it should be in the helpers folder formed as a class
@pytest.fixture
def test_email(request):
    try:
        params = request.params
        if params == 'free':
            return Faker().ascii_free_email()
        elif params == 'company':
            return Faker().ascii_company_email()
        else:
            raise NotImplementedError(f"Incorrect type of email: {params}")
    except AttributeError:
        return Faker().email()
