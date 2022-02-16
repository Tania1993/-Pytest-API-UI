import configparser
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

    def wait_until_element_present(self, by, value):
        try:
            element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((by, value)))
            return element
        except NoSuchElementException:
            return NoSuchElementException

