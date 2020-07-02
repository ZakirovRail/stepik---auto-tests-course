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
Preconditions - There is should be registered account 
Steps:
1. Run a browser
2. Select "Login or register"
2. Enter an email for authorisation 
3. Enter password for authorisation 
4. CLick on the "Enter" button

Expected result - Successful authorisation with a confirmation text on a page
"Thanks for registering!."

Post conditions - Delete just created account
"""

try:
    browser = webdriver.Chrome()
    browser.get(link)

    enter_registration = browser.find_element_by_id('login_link')
    enter_registration.click()

    # Проверяем что мы перешли на страницу авторизации/регистрации
    partial_title = "Войти или зарегистрироваться"
    button = WebDriverWait(browser, 5).until(
        EC.title_contains(partial_title)
    )

    if "Войти или зарегистрироваться" in browser.find_element_by_css_selector("ul.breadcrumb li.active").text:

        email_field = browser.find_element_by_css_selector('input#id_login-username.form-control')
        password_field = browser.find_element_by_css_selector('input#id_login-password.form-control')
        enter_button = browser.find_element_by_xpath("//button[@data-loading-text='Входим...']")

        # Вводим почту
        email_field.send_keys(email)
        # Вводим пароль
        password_field.send_keys(password)
        # Нажимаем кнопку для авторизации
        enter_button.click()
        time.sleep(2)

        alert_successful_auth = browser.find_element_by_css_selector("div.alertinner.wicon").text
        text_successful_auth = "Рады видеть вас снова"

        # Проверяем что текст об успещной авторизации присутствует
        if text_successful_auth not in alert_successful_auth:
            raise Exception("Wrong attempt for authorisation")
        else:
            print('Successful authorisation')

    else:
        print("wrong link to reg or auth")
finally:
    browser.quit()
