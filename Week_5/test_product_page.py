from .pages.product_page import ProductPage
import pytest

from time import sleep


# @pytest.mark.parametrize('link', ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     # link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_add_button()
#     page.should_be_book_name()
#     page.should_be_book_price()
#     page.add_good_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_be_info_message_about_adding()
#     page.should_be_equal_book_name()
#     page.should_be_equal_book_price()
#     sleep(1)

@pytest.mark.xfail(reason="clarify latter")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    :return:
    """
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_good_to_basket()
    page.should_not_be_element()


@pytest.mark.xfail(reason="clarify latter")
def test_guest_cant_see_success_message(browser):
    """
    Открываем страницу товара
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    :return:
    """
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_element()


@pytest.mark.xfail(reason="clarify latter")
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared
    :return:
    """
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_good_to_basket()
    page.is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_form()
    page.should_be_register_form()


if __name__ == '__main__':
    # test_guest_can_add_product_to_basket()
    test_guest_cant_see_success_message_after_adding_product_to_basket()
    test_guest_cant_see_success_message()
    test_message_disappeared_after_adding_product_to_basket()
    test_guest_should_see_login_link_on_product_page()
    test_guest_can_go_to_login_page_from_product_page()

# pytest -s test_product_page.py
