from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = 'https://suninjuly.github.io/execute_script.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    value = browser.find_element_by_id('input_value').text
    result = calc(value)
    # print(result)

    browser.find_element_by_css_selector('input.form-control').send_keys(result)

    check_box = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    check_box.click()

    # browser.execute_script("window.scrollBy(0, 100);")

    radio_button = browser.find_element_by_css_selector('[for="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
    radio_button.click()

    # browser.execute_script("window.scrollBy(0, 100);")
    submit_button = browser.find_element_by_css_selector('button.btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    time.sleep(4)

finally:
    browser.quit()
