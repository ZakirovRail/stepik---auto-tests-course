from .registration_page import RegPage
from .base_page import BasePage
from .welcome_page import WelcomePage
from time import time
from time import sleep


class TestRegistrationNewUser():
    def test_user_successfully_register(self, browser):
        email = str(time()) + "@fakemail.com"
        password = "Summercamp2020"
        print(email)
        print(password)

        link = "https://selenium1py.pythonanywhere.com"

        page = BasePage(browser, link)
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


if __name__ == '____main__':
    TestRegistrationNewUser()
# pytest --browser=Chrome --language=en-gb --alluredir=allure_report test_make_report.py
# allure serve allure_report
