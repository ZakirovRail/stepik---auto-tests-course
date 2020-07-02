from selenium import webdriver
import time
import math

link = "https://suninjuly.github.io/find_link_text"


def calculation() -> str:
    return str(math.ceil(math.pow(math.pi, math.e) * 10000))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    res_to_click = calculation()
    link = browser.find_element_by_partial_link_text(res_to_click)
    link.click()
    time.sleep(2)
    input1 = browser.find_element_by_name("first_name")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("input.form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(3)
    browser.quit()
