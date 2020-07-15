from .base_page import BasePage
from .locators import LoginPageLocators
from time import sleep
# from .main_page import MainPage


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        reg_email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        reg_email_field.send_keys(email)
        print('email entered')
        pass_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        pass_field.send_keys(password)
        print('password entered')
        conf_pass_field = self.browser.find_element(*LoginPageLocators.REG_CONF_PASSWORD)
        conf_pass_field.send_keys(password)
        print('confirmation password entered')
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()
        print('now will wait 3 seconds')
        sleep(3)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Login link is wrong"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"
