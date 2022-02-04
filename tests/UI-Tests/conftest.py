import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', default='en-gb',
                     help='Enter a language: en-gb, es, fr, ua, ru')


@pytest.fixture(scope='class')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    options = Options()
    if browser_name == 'chrome':
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser_name == 'firefox':
        # fp = webdriver.FirefoxProfile()
        # fp.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser

    browser.quit()
