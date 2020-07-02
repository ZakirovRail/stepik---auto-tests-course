from selenium import webdriver
import math
import time

link = 'https://suninjuly.github.io/math.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('input_value')
    x_element_text = x_element.text
    result = calc(x_element_text)

    answer_input = browser.find_element_by_id('answer')
    answer_input.clear()
    answer_input.send_keys(result)

    check_box = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    check_box.click()
    time.sleep(1)
    radio_button = browser.find_element_by_css_selector('[for="robotsRule"]')
    radio_button.click()

    time.sleep(1)

    submit_button = browser.find_element_by_css_selector('button.btn.btn-default')
    submit_button.click()

    time.sleep(3)
finally:
    browser.quit()
