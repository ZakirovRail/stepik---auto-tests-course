from logging import getLogger
import pytest

from faker import Faker
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Week_6_demo.constants import IMPLICIT_WAIT, WINDOWS_SIZE

logger = getLogger(__name__)


def pytest_addoption(parser):
    # parser.addoption('--browser', action='store', default='not_specified', help='Choose browser: chrome or firefox') # when run tests with default='not_specified'
    # falls with error _pytest.config.exceptions.UsageError: --browser_name should be chrome or firefox
    parser.addoption('--browser', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en-gb', help='Choose interface language.')


@pytest.fixture
def driver(request):
    browser = request.config.getoption('browser')
    user_language = request.config.getoption('language')
    if browser.lower() == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_language': user_language})
        driver = webdriver.Chrome(options=options)
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
        # TODO:implement language change
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')

    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.set_window_size(*WINDOWS_SIZE)
    yield driver
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
