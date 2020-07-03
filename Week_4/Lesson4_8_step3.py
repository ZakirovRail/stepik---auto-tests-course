import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import math

links_list = ["https://stepik.org/lesson/236895/step/1",
              "https://stepik.org/lesson/236896/step/1",
              "https://stepik.org/lesson/236897/step/1",
              "https://stepik.org/lesson/236898/step/1",
              "https://stepik.org/lesson/236899/step/1",
              "https://stepik.org/lesson/236903/step/1",
              "https://stepik.org/lesson/236904/step/1",
              "https://stepik.org/lesson/236905/step/1"]

s = ''


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', links_list)
def test_fantastic_messages(browser, link):
    open_link = "https://stepik.org/lesson/{link}}/step/1"
    browser.get(link)
    answer = math.log(int(time.time()))
    print("the answer is ", answer)

    # find the answer field
    answer_field = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area.ember-view")))

    # click the answer field and send the answer
    answer_field.clear()
    answer_field.send_keys(str(answer))
    print("the answer is sent")

    # wait while Submit button is available to click
    WebDriverWait(browser, 25).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))

    # click the Submit button
    submit_button = browser.find_element_by_css_selector("button.submit-submission")
    submit_button.click()
    print("the Submit button is clicked")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.attempt-message_correct"), "")
    )

    successful_text = browser.find_element_by_css_selector("span.attempt-message_correct").text
    print(successful_text)

    correct_text = browser.find_element_by_css_selector("pre.smart-hints__hint").text
    print(correct_text)

    global s
    if correct_text != "Correct!":
        s += correct_text
        print("\n" + s + "\n")

    assert correct_text == "Correct!", f"Wrong message for confirmation, expected 'Correct!', got {correct_text}"
