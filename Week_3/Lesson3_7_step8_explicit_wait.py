from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    browser.find_element_by_css_selector("button#book.btn.btn-primary").click()

    value = browser.find_element_by_css_selector('span#input_value').text
    print(value)

    result = calc(value)
    input_filed = browser.find_element_by_css_selector('input#answer')
    input_filed.send_keys(str(result))

    submit_button = browser.find_element_by_css_selector('button#solve.btn.btn-primary')
    submit_button.click()

    # message = browser.find_element_by_id("verify_message")
    # assert "successful" in message.text


finally:
    browser.quit()