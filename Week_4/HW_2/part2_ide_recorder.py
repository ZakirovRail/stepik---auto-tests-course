import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestSuccessfulregistration():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_successfulregistration(self):
        self.driver.get("https://selenium1py.pythonanywhere.com/ru/")
        self.driver.set_window_size(1550, 840)
        self.driver.find_element(By.ID, "login_link").click()
        self.driver.find_element(By.ID, "id_registration-email").click()
        self.driver.find_element(By.ID, "id_registration-email").send_keys("test2020+1@gmail.com")
        self.driver.find_element(By.ID, "id_registration-password1").click()
        self.driver.find_element(By.ID, "id_registration-password1").send_keys("tester1985")
        self.driver.find_element(By.ID, "id_registration-password2").send_keys("tester1985")
        self.driver.find_element(By.NAME, "registration_submit").click()
        self.driver.find_element(By.CSS_SELECTOR, ".alertinner").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".alertinner")
        assert len(elements) > 0
"""
Решил отдельный текстовый файл не создавать, чтобы не создавать лишних файлов. Опишу здесь.
Отличительные особенности:
1. вызов экземпляра драйвера через self - на мой взгляд делает менее удобочитаемым
2. Поиск локаторов через экземпляры класса By
3. Проверка наличия текста об успешной регистрации Селениум записал как проверку что текст присутствует. 
4. Селениум автоматически добавил неиспользуемые импорты
5. Селениум автоматически создал методы SetUp TearDown для класса TestSuccessfulregistration
6. Селениум автоматически создал словарь для переменных self.vars = {} в setup_method методе класса TestSuccessfulregistration
"""