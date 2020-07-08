from selenium import webdriver
from copy import deepcopy
from timeit import time

from locators import Reg_Locators
from locators import Auth_Locators

login_link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
email = 'test2020@gmail.com'
password = 'tester1985'
repeat_password = deepcopy(password)


def test_successful_registration_ru():
    registration_text = {
        'en-gb': 'Thanks for registering!',
        'ru': 'Спасибо за регистрацию!'
    }

    browser = webdriver.Chrome()
    # open a registration page
    browser.get(login_link)

    # maximize browser window
    browser.maximize_window()

    try:
        # enter the email
        browser.find_element(*Reg_Locators.reg_email).send_keys(email)

        # enter the password
        browser.find_element(*Reg_Locators.password).send_keys(password)

        # enter the confirmation password
        browser.find_element(*Reg_Locators.conf_password).send_keys(repeat_password)

        # click the Submit button
        browser.find_element(*Reg_Locators.register_button).click()

        success_message = browser.find_element(*Reg_Locators.messages).text.strip()
        print(success_message)

        # check the text about successful registration
        assert success_message == registration_text['ru'], 'Wrong registration text'

    finally:
        browser.quit()


def test_successful_authentication_ru():
    auth_text = {
        'en-gb': 'Nice to see you, again',
        'ru': 'Рады видеть вас снова'
    }
    try:

        browser = webdriver.Chrome()
        # open a registration page
        browser.get(login_link)

        # maximize browser window
        browser.maximize_window()


        # enter the email
        browser.find_element(*Auth_Locators.auth_email).send_keys(email)

        # enter the password
        browser.find_element(*Auth_Locators.auth_password).send_keys(password)

        # click to Enter button
        browser.find_element(*Auth_Locators.auth_button).click()

        success_auth_message = browser.find_element(*Auth_Locators.auth_messages).text.strip()
        print(success_auth_message)

        assert success_auth_message == auth_text[
            'ru'], f"Wrong authentication message, expected {auth_text['ru']}, got {success_auth_message}"

    finally:
        browser.quit()


if __name__ == '__main__':
    test_successful_registration_ru()
    test_successful_authentication_ru()
