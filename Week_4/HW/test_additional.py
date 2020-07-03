from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# additional work for evaluation


class TestRegistration:

    def test_successful_registration(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/ru/'
        email = 'test2020@gmail.com'
        password = 'tester1985'
        repeat_password = password

        # open browser
        browser.get(link)

        # Click on the enter or registration button
        enter_registration_button = WebDriverWait(browser, 25).until(EC.element_to_be_clickable((By.ID, "login_link")))

        enter_registration_button.click()

        # check that we are on the authorisation/registration page, continue,
        # else - print information about wrong redirection
        expected_title_text = "Войти или зарегистрироваться | Oscar - Sandbox"
        title_text = browser.title
        print(f"The page title is '{title_text}'")
        if expected_title_text == title_text:
            registration_button = browser.find_element_by_xpath("//button[@data-loading-text='Регистрация...']")
            email_field = browser.find_element_by_css_selector('input#id_registration-email.form-control')
            password_field = browser.find_element_by_css_selector('input#id_registration-password1.form-control')
            repeat_filed = browser.find_element_by_css_selector('input#id_registration-password2.form-control')

            # enter the email
            email_field.clear()
            email_field.send_keys(email)

            # enter the password
            password_field.clear()
            password_field.send_keys(password)

            # repeat the password
            repeat_filed.clear()
            repeat_filed.send_keys(repeat_password)

            # push the Submit button
            registration_button.click()

            # check that the registration was successful
            time.sleep(3)
            print("sleep for one minute")
            # if we don't see an error message, then should be redirected to a page with confirmation
            if browser.find_element_by_css_selector("div.alertinner.wicon").is_displayed():
                final_text = browser.find_element_by_css_selector("div.alertinner.wicon").text
                print(f"the final text of registration is '{final_text}'")
                text_for_check = "Спасибо за регистрацию!"

                # if we see expected text about successful registration, print a text
                if final_text == text_for_check:
                    print("Registration is over. Check the final text")
                else:
                    assert final_text == text_for_check, f"Wrong text after registration. Expected '{text_for_check}', " \
                                                         f"got the '{final_text}'"
            # if we see an error, print error message
            elif browser.find_element_by_css_selector("span.error-block").is_displayed():
                error_message_text = browser.find_element_by_css_selector("span.error-block").text
                # assert error_message_text
                print(f"There is an error during a registration. We got the '{error_message_text}'. "
                      f"Please, double check.")
                raise Exception(f"There is an error during a registration. We got the '{error_message_text}'. "
                      f"Please, double check.")
            else:
                print("Investigate the error")
        else:
            assert expected_title_text == title_text, f"Wrong redirection. " \
                                                      f"Expected a Authorisation/Registration page with a title " \
                                                      f"'{expected_title_text}', got '{title_text}'"

# pytest --language=es test_additional.py
# pytest --browser_name=chrome test_additional.py


"""
Прошу помочь объяснить почему, если я повторно запускаю тест по регистрации такого же пользователя,
то есть def test_successful_registration, то у меня выходит ошибка:
E       selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"div.alertinner.wicon"}
E         (Session info: chrome=83.0.4103.116)

Ругается на код строки 55. Но по идее мы не входим в это условие, мы должны переходить на строку 67. 
И можно ли в самих тестах использовать конструкцию raise Exception()? 
"""
