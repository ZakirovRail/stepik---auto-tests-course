from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import LoginPageLocators
from time import sleep
import allure


class LoginPage(BasePage):

    @allure.step('Check there is no error message about ')
    def should_not_be_existing_login_message(self):
        assert self.is_not_element_present(*ProductPageLocators.DUP_LOGIN_ERROR_MESSAGE), \
            "Error message about existing login during registration. Login should be unique"

    @allure.step('Register a new user')
    def register_new_user(self, email: str, password: str):
        reg_email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        reg_email_field.send_keys(email)
        pass_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        pass_field.send_keys(password)
        conf_pass_field = self.browser.find_element(*LoginPageLocators.REG_CONF_PASSWORD)
        conf_pass_field.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()
        self.should_not_be_existing_login_message()
        sleep(1)

    @allure.step('Check it is a login page')
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    @allure.step('Check there is a login url')
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Login link is wrong"

    @allure.step('Check there is a login form')
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    @allure.step('Check there is a register form')
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"
