from selenium.webdriver.common.by import By


class Reg_Locators:
    reg_email = (By.XPATH, '//input[@id="id_registration-email"]')
    password = (By.ID, 'id_registration-password1')
    conf_password = (By.ID, 'id_registration-password2')
    register_button = (By.NAME, 'registration_submit')
    messages = (By.CSS_SELECTOR, '#messages div div')


class Auth_Locators:
    auth_email = (By.XPATH, '//input[@id="id_login-username"]')
    auth_password = (By.XPATH, '//input[@id="id_login-password"]')
    auth_button = (By.XPATH, '//button[@value="Log In"]')
    auth_messages = (By.CSS_SELECTOR, '#messages div div')