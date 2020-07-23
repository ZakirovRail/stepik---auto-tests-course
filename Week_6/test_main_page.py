from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    @pytest.mark.need_review_custom_scenarios
    def test_guest_can_go_to_login_page(self, driver):
        link = "https://selenium1py.pythonanywhere.com/"
        page = MainPage(driver, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(driver, driver.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, driver):
        link = "https://selenium1py.pythonanywhere.com/"
        page = MainPage(driver, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.need_review_custom_scenarios
def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    link = "https://selenium1py.pythonanywhere.com/"
    page = MainPage(driver, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_text_about_empty_basket()


# if __name__ == '____main__':
#     TestLoginFromMainPage.test_guest_can_go_to_login_page()
#     TestLoginFromMainPage.test_guest_should_see_login_link()
#     test_guest_cant_see_product_in_basket_opened_from_main_page()

# pytest -v --tb=line --language=en test_main_page.py
# pytest -v --tb=line --language=en --browser=firefox test_main_page.py
