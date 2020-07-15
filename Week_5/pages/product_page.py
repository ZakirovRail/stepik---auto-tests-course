from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ProductPageLocators


# from .basket_page import BasketPage


class ProductPage(BasePage):

    def should_be_add_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), "The 'Add to basket' button is not presented"

    def should_be_book_name(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "The book name is not presented"

    def should_be_book_price(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "The price for the book is not presented"
        # вопрос как возвращать полученное значение и потом принимать его как входной параметр в следующей проверке?

    def add_good_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_info_message_about_adding(self):
        # info_message = self.browser.find_element(*ProductPageLocators.ABOUT_ADDING_MESSAGE)
        assert self.is_element_present(
            *ProductPageLocators.ABOUT_ADDING_MESSAGE), "No message about successful adding of a book to the asket"

    def should_be_equal_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_name == self.browser.find_element(
            *ProductPageLocators.ADDED_BOOK_NAME).text, "The name of added book is not equal to expected name"

    def should_be_equal_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert book_price == self.browser.find_element(
            *ProductPageLocators.ADDED_BOOK_PRICE).text, "The total price in the basket is not equal as a price for the " \
                                                         "added book"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located(*ProductPageLocators.ADDED_BOOK_NAME))
        except TimeoutException:
            return False
        return True

    def should_not_be_element(self):
        assert BasePage.is_not_element_present(*ProductPageLocators.ADDED_BOOK_NAME), "Login link is not presented"
