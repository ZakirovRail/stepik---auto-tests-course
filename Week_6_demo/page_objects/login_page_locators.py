from selenium.webdriver.common.by import By


class LoginPageLocators:
    email_field = (By.ID, 'id_registration-email')
    pwd1_field = (By.ID, 'id_registration-password1')
    pwd2_field = (By.ID, 'id_registration-password2')
    register_btn = (By.NAME, 'registration_submit')
