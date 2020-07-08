import pytest
from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# browser = webdriver.Chrome()
# link = "https://stepik.org/lesson/236896/step/1"
# browser.get(link)
#
# # calculte the answer
# answer = math.log(int(time.time()))
# print("the answer is ", answer)
# print(type(answer))
#
# # find the answer field
# WebDriverWait(browser, 5).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.ember-text-area.ember-view")))
#
# # click the answer field and send the answer
# answer_field = browser.find_element_by_class_name("textarea.ember-text-area.ember-view")
# answer_field.clear()
# answer_field.send_keys(str(answer))
# print("the answer is sent")
#
# # wait while Submit button is available to click
# WebDriverWait(browser, 5).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
#
# # click the Submit button
# submit_button = browser.find_element_by_css_selector("button.submit-submission")
# submit_button.click()
# print("the button is clicked")
# time.sleep(10)
#======================================================================================================================
# WebDriverWait(browser, 12).until(
#             EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.attempt-message_correct"), "")
#         )

# successful_text = browser.find_element_by_css_selector("span.attempt-message_correct").text
# print(successful_text)
#
# correct_text = browser.find_element_by_css_selector("pre.smart-hints__hint").text
# print(correct_text)
#
# assert correct_text == "Correct!", f"Wrong message for confirmation, expected 'Correct!', got {correct_text}"
#
# time.sleep(120)
# browser.quit()
#======================================================================================================================


browser = webdriver.Chrome()
link = "https://selenium1py.pythonanywhere.com/ru/"
browser.get(link)

enter_registration_button = WebDriverWait(browser, 25).until \
    (EC.element_to_be_clickable((By.ID, "login_link")))

enter_registration_button.click()

expected_title_text = "    Войти или зарегистрироваться | Oscar - Sandbox!!!"
title_text = browser.find_element_by_css_selector("head > title").text
print(type(title_text))
print('===========')