from selenium import webdriver
import time
import math

link = ('https://suninjuly.github.io/redirect_accept.html')


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    flying_button = browser.find_element_by_css_selector('button.trollface.btn.btn-primary')
    flying_button.click()

    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)


    value = browser.find_element_by_id('input_value').text
    result = calc(value)

    input_filed = browser.find_element_by_css_selector('input#answer')
    input_filed.send_keys(result)

    submit_button = browser.find_element_by_css_selector('button.btn.btn-primary')
    submit_button.click()

    time.sleep(5)


finally:
    browser.quit()
