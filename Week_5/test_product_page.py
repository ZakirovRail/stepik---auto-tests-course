from .pages.product_page import ProductPage
from .pages.locators import GoodsPageLocators

from time import sleep


def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
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
    sleep(2)


if __name__ == '__main__':
    test_guest_can_add_product_to_basket()

# pytest -s test_product_page.py
