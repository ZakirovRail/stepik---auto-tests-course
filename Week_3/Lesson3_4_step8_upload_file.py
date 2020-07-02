from selenium import webdriver
import os
import time

link = 'https://suninjuly.github.io/file_input.html'

try:

    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'empty.txt')

    first_name = browser.find_element_by_xpath("//input[@placeholder='Enter first name']")
    first_name.send_keys('First_Name')

    last_name = browser.find_element_by_xpath("//input[@placeholder='Enter last name']")
    last_name.send_keys('Last_Name')

    email_data = browser.find_element_by_xpath("//input[@placeholder='Enter email']")
    email_data.send_keys('random_email@gmail.com')

    choose_file_button = browser.find_element_by_css_selector('input#file')
    choose_file_button.send_keys(file_path)

    submit_button = browser.find_element_by_css_selector('button.btn.btn-primary')
    submit_button.click()

    time.sleep(4)

finally:
    browser.quit()
