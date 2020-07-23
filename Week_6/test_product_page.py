from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
import pytest
from time import sleep
import time
from random import randint


email = str(time.time())+str(randint(0, 15000)) + "@fakemail.org"
print(email)
password = 'Summer2020'


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        link = "https://selenium1py.pythonanywhere.com/"
        page = MainPage(driver, link)
        page.open()
        page.go_to_login_page()
        reg_page = LoginPage(driver, driver.current_url)
        reg_page.register_new_user(email, password)
        # print('registration successful')
        reg_page.should_be_authorized_user()
        sleep(1)

    # @pytest.mark.need_review_custom_scenarios
    # @pytest.mark.xfail(reason="clarify latter")  # fails on registration step - there is existing login
    # def test_user_cant_see_success_message(self, driver):
    #     link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    #     page = ProductPage(driver, link)
    #     page.open()
    #     page.should_not_be_element()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
        page = ProductPage(driver, link)
        page.open()
        page.should_be_add_button()
        page.should_be_book_name()
        page.should_be_book_price()
        page.add_good_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_info_message_about_adding()
        page.should_be_equal_book_name()
        page.should_be_equal_book_price()


@pytest.mark.xfail(reason="clarify latter") # XFAIL
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


@pytest.mark.parametrize('link',
                         ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", # test for link with offer7 FAILS - Book name contains word "book"
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(driver, link): # REQUIRED
    # link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = ProductPage(driver, link)
    page.open()
    page.should_be_add_button()
    page.should_be_book_name()
    page.should_be_book_price()
    page.add_good_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_info_message_about_adding()
    page.should_be_equal_book_name() #  # test for link with offer7 FAILS - Book name contains word "book"
    page.should_be_equal_book_price()


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

@pytest.mark.need_review_custom_scenarios
def test_guest_should_see_login_link_on_product_page(driver):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_form()
    page.should_be_register_form()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    """
    Гость открывает страницу товара
    Переходит в корзину по кнопке в шапке
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста
    :return:
    """
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_text_about_empty_basket()



# pytest -s test_product_page.py
# pytest -v --tb=line --language=en test_product_page.py
# pytest -v --tb=line --language=en --browser=firefox test_product_page.py
