import configparser
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    config = configparser.ConfigParser()
    config.read('config.ini')
    link = config['URLs']['selenium_test_page']

    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self, url=link):
        self.browser.get(f'{url}/')

    def is_element_present(self, by, value):
        try:
            self.browser.find_element(by, value)
        except NoSuchElementException:
            return NoSuchElementException
        return True

