import unittest
from selenium import webdriver
import time


class TestNew(unittest.TestCase):
    def test_new_check_page(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector(
            ".first_block .form-group.first_class:nth-child(1) .form-control.first").send_keys("Ivan")
        browser.find_element_by_css_selector("input.form-control.second").send_keys("Petrov")
        browser.find_element_by_css_selector("input.form-control.third").send_keys("Smolensk")
        browser.find_element_by_xpath("//input[@placeholder='Input your phone:']").send_keys("123456789")
        browser.find_element_by_xpath("//input[@placeholder='Input your address:']").send_keys("Random address")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Wrong text in welcome text")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()

# 1 failed, 1 passed in 21.95s