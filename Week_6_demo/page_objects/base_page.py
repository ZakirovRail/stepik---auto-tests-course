from logging import getLogger
from urllib.parse import urljoin

import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# from constants import BASE_URL, EXPLICIT_WAIT
from Week_6_demo.constants import BASE_URL, EXPLICIT_WAIT

logger = getLogger(__name__)


class BasePage():
    _base_url = BASE_URL
    _page_path = None

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def url(self):
        return self._driver.current_url

    @property
    def source(self):
        return self._driver.page_source

    def open(self):
        url = urljoin(self._base_url, self._page_path)
        with allure.step(f'open {url}'):
            self._driver.get(url)

    def is_element_present(self, locator: tuple) -> bool:
        return len(self._driver.find_elements(*locator)) > 0

    def find_element(self, locator: tuple) -> WebElement:
        try:
            element = self._driver.find_element(*locator)
            return element
        except NoSuchElementException:
            raise AssertionError(f'Element with locator: {locator} not found')

    def wait_until_element_invisible(self, locator: tuple, timeout=EXPLICIT_WAIT):
        try:
            return WebDriverWait(self._driver, timeout).until(
                EC.invisibility_of_element_located(locator),
                "Element with locator: {0}:{1} still visible".format(*locator)
            )
        except TimeoutException as e:
            raise AssertionError(e)

# only for testing local initialisation
# if __name__ == '__main__':
#     from selenium import webdriver
#     from time import sleep
#
#     driver = webdriver.Chrome()
#     bp = BasePage(driver=driver)
#     sleep(5)
#     bp.open()
