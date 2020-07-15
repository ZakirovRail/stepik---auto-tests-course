from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input.form-control[type='email'][name='login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input.form-control[type='password'][name='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary[value='Log In']")

    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "input.form-control[type='email'][name='registration-email']")
    REG_PASSWORD = (By.CSS_SELECTOR, "input.form-control[type='password'][name='registration-password1']")
    REG_CONF_PASSWORD = (By.CSS_SELECTOR, "input.form-control[type='password'][name='registration-password2']")
    REG_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary[value='Register']")

    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > a.btn.btn-default")
    BASKET_DROP_DOWN = (By.CSS_SELECTOR, "button.btn.btn-default.dropdown-toggle")


class ProductPageLocators():
    WRITE_REVIEW = (By.CSS_SELECTOR, "#write_review.btn.btn-success.btn-sm")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket[type='submit']")
    ADD_TO_WISH_LIST = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-wishlist")
    BOOK_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")
    ABOUT_ADDING_MESSAGE = (
        By.CSS_SELECTOR, "#messages div.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1)")
    ADDED_BOOK_NAME = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) strong")
    ADDED_BOOK_PRICE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators():
    BASKET_LABEL_TEXT = (By.CSS_SELECTOR, "div.page-header.action > h1")
    TEXT_ABOUT_EMPTINESS = (By.CSS_SELECTOR, "div#content_inner p")
    LINK_CONTINUE_SHOPPING = (By.CSS_SELECTOR, "div#content_inner p > a")
    ITEMS_TO_BUY_NOW = (By.CSS_SELECTOR, "div.row > h2.col-sm-6.h3")
