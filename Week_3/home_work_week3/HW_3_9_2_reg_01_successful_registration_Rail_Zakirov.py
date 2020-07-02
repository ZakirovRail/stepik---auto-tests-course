from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://selenium1py.pythonanywhere.com/ru/'
email = 'test2020@gmail.com'
password = 'tester1985'
repeat_password = password

# здесь в других файлах специально поставил time задержку, потом их удалю заменю на ожидания

"""
Steps:
1. Run a browser
2. Select "Login or register"
2. Enter an email
3. Enter password
4. Enter confirmation password
5. CLick on the "Register" button

Expected result - Successful registration with a confirmation text on a page
"Рады видеть вас снова"
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

    # Проверяем что есть раздел регистрации
    if registration_title.is_displayed():
        assert registration_title.text == 'Зарегистрироваться'

        # Вводим адрес
        email_field.clear()
        email_field.send_keys(email)
        time.sleep(1)

        # Вводим сложный пароль
        password_field.clear()
        password_field.send_keys(password)
        time.sleep(1)

        # Вводим повторно пароль для проверки
        repeat_filed.clear()
        repeat_filed.send_keys(repeat_password)
        time.sleep(1)

        # Нажимаем кнопку для окончания регистрации
        registration_button.click()
        time.sleep(5)

        final_text = browser.find_element_by_css_selector("div.alertinner.wicon").text
        text_for_check = "Спасибо за регистрацию!"
        # Проверяем что есть текст об успешной регистрации
        if final_text is True:
            assert text_for_check in final_text, "Wrong text after registration"
            print("Successful registration")
        else:
            assert "Registration is failed"
    else:
        print('The current page is not a Registration page. Something is wrong')

finally:
    browser.quit()
