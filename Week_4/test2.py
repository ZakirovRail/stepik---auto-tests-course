import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

s = ''


@pytest.mark.parametrize('par', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestLogin(object):
    def test_feedback(self, browser, par):
        link = f"https://stepik.org/lesson/{par}/step/1"
        browser.get(link)
        browser.implicitly_wait(30)

        # ищем элемент со строкой для ввода и передаем туда значение
        answer = browser.find_element_by_css_selector(".textarea")
        answer.send_keys(str(math.log(int(time.time()))))
        button = browser.find_element_by_css_selector("button.submit-submission")
        button.click()

        # ожидаем, пока результат появится на экране
        res = WebDriverWait(browser, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".textarea")))

        # передаем текст результата в result_text
        result = browser.find_element_by_css_selector(".smart-hints__hint")
        result_text = result.text

        # сравниваем фактический результат с ожидаемым. Если отличается, то добавляем в строку s и выводим на экран
        global s
        if result_text != "Correct!":
            s += result_text
            print( "\n" + s + "\n" )

        assert result_text == "Correct!", \
            f"Wrong result, got '{result_text}' instead of 'Correct!'"

