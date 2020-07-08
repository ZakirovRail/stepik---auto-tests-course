import time

class TestGoods:

    def test_add_button_exists(self, browser):
        link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        button_here = browser.find_element_by_css_selector("button.btn-add-to-basket")
        assert button_here, "Button not found"
        time.sleep(2)

# pytest -s --language=es test_items.py
# pytest -s --language=fr test_items.py
