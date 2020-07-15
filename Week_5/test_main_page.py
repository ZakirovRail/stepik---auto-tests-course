from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(self, browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(self, browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Гость открывает главную страницу
    Переходит в корзину по кнопке в шапке сайта
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста
    :return:
    """
    link = "https://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_text_about_empty_basket()


if __name__ == '____main__':
    test_guest_can_go_to_login_page()
    test_guest_should_see_login_link()
    test_guest_cant_see_product_in_basket_opened_from_main_page()

# pytest -v --tb=line --language=en test_main_page.py
