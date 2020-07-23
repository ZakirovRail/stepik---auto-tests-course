import pytest
from Week_6_demo.page_objects.login_page import LoginPage


class TestLoginPage:
    @pytest.mark.parametrize(
        'test_email, pwd', [
            pytest.param('free', 'xxxXXX1234', id='Free email'),
            pytest.param('company', 'xxxXXX1234', id='Company email')
        ], indirect=['test_email']
    )
    def test_valid_login(self, driver, test_email, pwd):
        lp = LoginPage(driver)
        lp.open()
        lp.register(test_email, pwd, pwd)
