from selenium import webdriver
import math
import time

link = 'https://suninjuly.github.io/get_attribute.html'


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('treasure')
    treasure_val = x_element.get_attribute('valuex')

    calc_res = calc(treasure_val)

    answer_input = browser.find_element_by_id('answer')
    answer_input.clear()
    answer_input.send_keys(calc_res)

    check_box = browser.find_element_by_id('robotCheckbox')
    check_box.click()

    radio_button = browser.find_element_by_id('robotsRule')
    radio_button.click()

    submit_button = browser.find_element_by_css_selector('button.btn.btn-default')
    submit_button.click()

    time.sleep(4)
finally:
    browser.quit()
