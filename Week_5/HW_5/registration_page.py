from .locators import RegPageLocators
from .base_page import BasePage


class RegPage(BasePage):
    def register_new_user(self, email, password):
        reg_email_field = self.browser.find_element(*RegPageLocators.REG_EMAIL)
        reg_email_field.send_keys(email)
        print('email entered')
        pass_field = self.browser.find_element(*RegPageLocators.REG_PASSWORD)
        pass_field.send_keys(password)
        print('password entered')
        conf_pass_field = self.browser.find_element(*RegPageLocators.REG_CONF_PASSWORD)
        conf_pass_field.send_keys(password)
        print('confirmation password entered')
        reg_button = self.browser.find_element(*RegPageLocators.REG_BUTTON)
        reg_button.click()
        print('now will wait 3 seconds')
