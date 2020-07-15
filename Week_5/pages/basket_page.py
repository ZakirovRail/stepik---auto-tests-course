from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_basket_label(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_LABEL_TEXT), "Basket label text is not presented"

    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.TEXT_ABOUT_EMPTINESS), "Text that the basket is empty is not presented"

    def should_be_link_continue_shopping(self):
        assert self.is_element_present(
            *BasketPageLocators.LINK_CONTINUE_SHOPPING), "No link to continue shopping is not presented"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.ITEMS_TO_BUY_NOW), "The basket is not empty, but should be"
