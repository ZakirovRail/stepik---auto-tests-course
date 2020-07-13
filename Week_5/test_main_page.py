def test_guest_can_go_to_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()


if __name__ == '____main__':
    test_guest_can_go_to_login_page()

# pytest -v --tb=line --language=en test_main_page.py
