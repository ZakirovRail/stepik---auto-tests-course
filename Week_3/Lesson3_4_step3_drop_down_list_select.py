from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'https://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num_1 = browser.find_element_by_id('num1').text
    num_2 = browser.find_element_by_id('num2').text
    sum_num = int(num_1) + int(num_2)

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(str(sum_num))

    submit_button = browser.find_element_by_css_selector('button.btn.btn-default')
    submit_button.click()

    time.sleep(4)
finally:
    browser.quit()
