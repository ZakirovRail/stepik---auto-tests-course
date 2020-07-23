import allure
from Week_6_demo.page_objects.base_page import BasePage
from Week_6_demo.page_objects.login_page_locators import LoginPageLocators as LPL


class LoginPage(BasePage):
    _page_path = '/accounts/login'

    @allure.step('Register user')
    def register(self, email: str, pwd1: str, pwd2: str):
        self.find_element(LPL.email_field).send_keys(email)
        self.find_element(LPL.pwd1_field).send_keys(pwd1)
        self.find_element(LPL.pwd2_field).send_keys(pwd2)
        self.find_element(LPL.register_btn).click()
        self.wait_until_element_invisible(LPL.register_btn)
