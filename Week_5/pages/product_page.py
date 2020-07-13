from .base_page import BasePage
from .locators import GoodsPageLocators


class ProductPage(BasePage):

    def should_be_add_button(self):
        assert self.is_element_present(
            *GoodsPageLocators.ADD_TO_BASKET_BUTTON), "The 'Add to basket' button is not presented"

    def should_be_book_name(self):
        assert self.is_element_present(*GoodsPageLocators.BOOK_NAME), "The book name is not presented"

    def should_be_book_price(self):
        assert self.is_element_present(*GoodsPageLocators.BOOK_PRICE), "The price for the book is not presented"
        # вопрос как возвращать полученное значение и потом принимать его как входной параметр в следующей проверке?

    def add_good_to_basket(self):
        add_button = self.browser.find_element(*GoodsPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_info_message_about_adding(self):
        # info_message = self.browser.find_element(*GoodsPageLocators.ABOUT_ADDING_MESSAGE)
        assert self.is_element_present(
            *GoodsPageLocators.ABOUT_ADDING_MESSAGE), "No message about successful adding of a book to the asket"

    def should_be_equal_book_name(self):
        book_name = self.browser.find_element(*GoodsPageLocators.BOOK_NAME).text
        assert book_name == self.browser.find_element(
            *GoodsPageLocators.ADDED_BOOK_NAME).text, "The name of added book is not equal to expected name"

    def should_be_equal_book_price(self):
        book_price = self.browser.find_element(*GoodsPageLocators.BOOK_PRICE).text
        assert book_price == self.browser.find_element(
            *GoodsPageLocators.ADDED_BOOK_PRICE).text, "The total price in the basket is not equal as a price for the " \
                                                       "added book"
