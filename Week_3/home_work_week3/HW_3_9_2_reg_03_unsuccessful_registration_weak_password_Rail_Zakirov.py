from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://selenium1py.pythonanywhere.com/ru/'
email = 'test2020@gmail.com'
password = 'testeq'
repeat_password = password

# здесь в других файлах специально поставил time задержку, потом их удалю


"""
Steps:
1. Run a browser
2. Select "Login or register"
2. Enter an existing email
3. Enter a weak password (the password is less then 9 symbols), example "testeq"
4. Enter confirmation password (the password is less then 9 symbols), example "testeq"
5. Click on the "Register" button

Expected result:
1. There is the error massage about existing user with such email
"Опаньки! Мы нашли какие-то ошибки - пожалуйста, проверьте сообщения об ошибках ниже и попробуйте еще раз"
2. There is the alert below the "Введённый пароль слишком короткий. Он должен содержать как минимум 9 символов."
"""

try:
    browser = webdriver.Chrome()
    browser.get(link)

    oscar_link = browser.find_element_by_css_selector('div.col-sm-7.h1 a').text

    assert oscar_link == 'Oscar', 'There is no link for Oscar'
    sandbox_title = browser.find_element_by_css_selector('div.col-sm-7.h1 small').text

    assert sandbox_title == 'Sandbox', 'There is no title Sandbox'

    enter_registration = browser.find_element_by_id('login_link')
    enter_registration.click()

    # Проверяем что мы перешли на страницу авторизации/регистрации
    partial_title = "Войти или зарегистрироваться"
    button = WebDriverWait(browser, 5).until(
        EC.title_contains(partial_title)
    )

    registration_title = browser.find_element_by_css_selector('#register_form h2')
    registration_button = browser.find_element_by_xpath("//button[@data-loading-text='Регистрация...']")
    email_field = browser.find_element_by_css_selector('input#id_registration-email.form-control')
    password_field = browser.find_element_by_css_selector('input#id_registration-password1.form-control')
    repeat_filed = browser.find_element_by_css_selector('input#id_registration-password2.form-control')

    if registration_title.is_displayed():
        assert registration_title.text == 'Зарегистрироваться'
        email_field.clear()
        email_field.send_keys(email)
        time.sleep(1)

        password_field.clear()
        password_field.send_keys(password)
        time.sleep(1)

        repeat_filed.clear()
        repeat_filed.send_keys(repeat_password)
        time.sleep(1)

        registration_button.click()
        time.sleep(5)

        register_error_message_text = browser.find_element_by_css_selector("div.alert.alert-danger").text
        error_message_text = browser.find_element_by_css_selector("span.error-block").text

        print(register_error_message_text)
        print(error_message_text)

        text_for_check_in_register = "Опаньки! Мы нашли какие-то ошибки - пожалуйста, " \
                                     "проверьте сообщения об ошибках ниже и попробуйте еще раз"
        text_for_check_alert = "Введённый пароль слишком короткий. Он должен содержать как минимум 9 символов."

        if (register_error_message_text is True) and (error_message_text is True):
            assert text_for_check_in_register in register_error_message_text, \
                "Wrong text after failed registration with weak password"

            assert text_for_check_alert in error_message_text, \
                "Wrong text in alert after failed registration with weak password"
        else:
            assert "error message or alert did not appear"
    else:
        print('The current page is not a Registration page. Something is wrong')

finally:
    browser.quit()
