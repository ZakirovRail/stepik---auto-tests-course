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
    REG_BUTTON = (By.CSS_SELECTOR, "#button.btn.btn-lg.btn-primary[value='Register']")
