from .base_page import BasePage
from .locators import WelcomePageLocators


class WelcomePage(BasePage):
    def should_be_welcome_text(self):
        assert self.is_element_present(*WelcomePageLocators.WELCOME_TEXT), "The 'Welcome' text is not presented"

    def should_be_thanks_text(self):
        assert self.is_element_present(
            *WelcomePageLocators.THANKS_TEXT), "The 'Thanks for registering!' text is not presented"
