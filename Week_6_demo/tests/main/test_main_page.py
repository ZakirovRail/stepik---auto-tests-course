from Week_6_demo.page_objects.main_page import MainPage


class TestMainPage:
    def test_login_link_exist(self, driver):
        mp = MainPage(driver=driver)
        mp.open()
        assert mp.login_link_exist(), 'Login link not exists'

    def test_can_open_login_page_from_main_page(self, driver):
        mp = MainPage(driver)
        mp.open()
        mp.enter_or_register()
        assert 'accounts/login' in mp.url, 'Incorrect link'
