import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# define  a command line options
def pytest_addoption(parser):
    parser.addoption('--type_browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: ru, en, fr, es and etc.")


@pytest.fixture(scope="function")
def browser(request):
    type_browser = request.config.getoption("type_browser")
    user_language = request.config.getoption("language")
    browser = None
    if type_browser == "chrome":
        print(f"\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif type_browser == "firefox":
        print(f"\nstart {type_browser} browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--type_browser should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
"""
Этот файл conftest.py и файл test_items.py лежат в подпапке HW  каталога Week_4.
В каталоге Week_4 есть пустой файл conftest.py
Дело в том, что когда я удаляю файл conftest.py из папки Week_4,то запуск тестов падает
# pytest -s --language=es test_items.py
# pytest -s --language=fr test_items.py

Если я оставляю пустой conftest.py из папки Week_4 и текущий файл conftest.py, то тесты проходят успешно.
В чем моет быть дело?
"""