from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
3. Enter an email for authorisation 
4. Enter password for authorisation 
5. Click on the "Enter" button
6. Select "All goods" from the "Review of market" dropdown

Expected result - A user is redirected to a page "All goods"

"""

try:
    browser = webdriver.Chrome()
    browser.get(link)

    enter_registration = browser.find_element_by_id('login_link')
    enter_registration.click()

    # Проверяем что мы перешли на страницу авторизации/регистрации
    partial_title = "Войти или зарегистрироваться"
    button = WebDriverWait(browser, 3).until(
        EC.title_contains(partial_title)
    )
    time.sleep(1)
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
        time.sleep(1)

        alert_successful_auth = browser.find_element_by_css_selector("div.alertinner.wicon").text
        text_successful_auth = "Рады видеть вас снова"
        time.sleep(1)
        # Проверяем что текст об успешной авторизации присутствует
        if text_successful_auth not in alert_successful_auth:
            raise Exception("Wrong attempt for authorisation")
        else:
            lang_drop_down = browser.find_element_by_css_selector("select.form-control option")
            lang_drop_down_ru = browser.find_element_by_css_selector("select.form-control option[value='ru']")
            lang_drop_down_attr = lang_drop_down_ru.get_attribute("selected")
            time.sleep(1)
            # Проверяем если язык не русский - то есть None
            if lang_drop_down_attr is None:
                # Открываем dropdown
                lang_drop_down.click()
                # Выбираем русский язык
                lang_drop_down_ru.click()
                # Нажимаем  кнопку подветрждения выбора языка
                go_button = browser.find_element_by_css_selector("button.btn.btn-default[type='submit']")
                go_button.click()
                time.sleep(2)
                print("Selected language is 'Russian' ")

                # говорим Selenium проверять в течение 3 секунд, что
                all_goods_link = WebDriverWait(browser, 3).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Все товары')]"))
                )

                # выбираем раздел "Все товары"
                all_goods_link.click()

                # Проверяем что мы перешли на страницу "Все товары"
                partial_title_allgoods = "Все товары"
                button = WebDriverWait(browser, 5).until(
                    EC.title_contains(partial_title_allgoods)
                )
            else:
                all_goods_link = WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Все товары')]"))
                )

                # выбираем раздел "Все товары"
                all_goods_link.click()

                # Проверяем что мы перешли на страницу "Все товары"
                partial_title_allgoods = "Все товары"
                button = WebDriverWait(browser, 5).until(
                    EC.title_contains(partial_title_allgoods)
                )
    else:
        print("wrong link to reg or auth")
finally:
    browser.quit()
