from .pages.product_page import ProductPage
from .pages.locators import GoodsPageLocators
import pytest

from time import sleep


@pytest.mark.parametrize('link', ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_button()
    page.should_be_book_name()
    page.should_be_book_price()
    page.add_good_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_info_message_about_adding()
    page.should_be_equal_book_name()
    page.should_be_equal_book_price()
    sleep(1)


if __name__ == '__main__':
    test_guest_can_add_product_to_basket()

# pytest -s test_product_page.py
