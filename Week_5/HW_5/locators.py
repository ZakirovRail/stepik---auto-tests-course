from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class RegPageLocators():
    REG_EMAIL = (By.CSS_SELECTOR, "input.form-control[type='email'][name='registration-email']")
    REG_PASSWORD = (By.CSS_SELECTOR, "input.form-control[type='password'][name='registration-password1']")
    REG_CONF_PASSWORD = (By.CSS_SELECTOR, "input.form-control[type='password'][name='registration-password2']")
    REG_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary[value='Register']")


class WelcomePageLocators():
    WELCOME_TEXT = (By.CSS_SELECTOR, "#promotions section.well.well-blank div.sub-header h2")
    THANKS_TEXT = (By.CSS_SELECTOR, "div.alertinner.wicon")
