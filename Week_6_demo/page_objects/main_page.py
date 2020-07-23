import allure
from Week_6_demo.page_objects.base_page import BasePage
from Week_6_demo.page_objects.main_page_locators import MainPageLocators as MPL


class MainPage(BasePage):
    @allure.step('Search product')
    def search(self, text_to_search:str):
        self.find_element(MPL.search_field).send_keys(text_to_search)
        self.find_element(MPL.search_button).click()

    def enter_or_register(self):
        self.find_element(MPL.login_link).click()

    def login_link_exist(self) -> bool:
        return self.is_element_present(MPL.login_link)
