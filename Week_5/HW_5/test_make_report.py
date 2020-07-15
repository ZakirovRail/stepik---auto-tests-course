from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from time import time
from time import sleep

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class RegPageLocators():
    REG_EMAIL = (By.CSS_SELECTOR, "input.form-control[type='email'][name='registration-email']")
    REG_PASSWORD = (By.CSS_SELECTOR, "input.form-control[type='password'][name='registration-password1']")
    REG_CONF_PASSWORD = (By.CSS_SELECTOR, "input.form-control[type='password'][name='registration-password2']")
    REG_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary[value='Register']")


class WelcomePageLocators():
    WELCOME_TEXT = (By.CSS_SELECTOR, "#promotions section.well.well-blank:nth-child(1) > div.sub-header > h2")
    THANKS_TEXT = (By.CSS_SELECTOR, "div.alertinner.wicon")


class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True


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
        # sleep(3)


class WelcomePage(BasePage):
    def should_be_welcome_text(self):
        assert self.is_element_present(*WelcomePageLocators.WELCOME_TEXT), "The 'Welcome' text is not presented"

    def should_be_thanks_text(self):
        assert self.is_element_present(
            *WelcomePageLocators.THANKS_TEXT), "The 'Thanks for registering!' text is not presented"


class TestRegistrationNewUser():
    def test_user_successfully_register(self, browser):
        email = str(time()) + "@fakemail.com"
        password = "Summercamp2020"
        print(email)
        print(password)

        link = "https://selenium1py.pythonanywhere.com"

        page = BasePage(browser,link)
        page.open()
        print('we should be on MAIN page')
        sleep(1)
        page.go_to_login_page()
        print('we should be on Registration page')
        print('sleep 2 seconds')
        sleep(1)

        reg_page = RegPage(browser, browser.current_url)
        reg_page.register_new_user(email, password)

        wel_page = WelcomePage(browser, browser.current_url)
        wel_page.should_be_welcome_text()
        wel_page.should_be_thanks_text()

# pytest --browser=Chrome --language=en-gb --alluredir=allure_report test_make_report.py
# allure serve allure_report
