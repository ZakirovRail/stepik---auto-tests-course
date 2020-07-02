from selenium import webdriver
import math
import time

link = ('https://suninjuly.github.io/alert_accept.html')


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    i_want_button = browser.find_element_by_css_selector('button.btn.btn-primary')
    i_want_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    value = browser.find_element_by_id('input_value').text
    result = calc(value)

    input_filed = browser.find_element_by_css_selector('input#answer')
    input_filed.send_keys(result)

    submit_button = browser.find_element_by_css_selector('button.btn.btn-primary')
    submit_button.click()

    time.sleep(5)

finally:
    browser.quit()
