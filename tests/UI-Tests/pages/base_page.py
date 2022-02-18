import configparser
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    config = configparser.ConfigParser()
    config.read('config.ini')
    link = config['URLs']['selenium_test_page']

    LOGIN_LINK_CSS_SELECTOR = (By.CSS_SELECTOR, '#login_link')
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini .btn-group > a')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button.favorite')

    def __init__(self, browser):
        self.browser = browser

    def open(self, url=link, timeout=10):
        print("type " + str(type(self.browser)))
        self.browser.implicitly_wait(timeout)
        self.browser.get(f'{url}/')

    def page_should_be_opened(self, str):
        return str in self.browser.current_url

    def is_element_present(self, by, value):
        try:
            self.browser.find_element(by, value)
        except NoSuchElementException:
            return NoSuchElementException
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def wait_until_element_present(self, by, value):
        try:
            element = WebDriverWait(self.browser, 10.0).until(EC.visibility_of_element_located((by, value)))
            return element
        except NoSuchElementException:
            return NoSuchElementException

    def click_login_link(self):
        login_link = self.browser.find_element(*self.LOGIN_LINK_CSS_SELECTOR)
        login_link.click()

    def login_link_should_be_present(self):
        return self.is_element_present(*self.LOGIN_LINK_CSS_SELECTOR)

    def basket_link_should_be_present(self):
        return self.is_element_present(*self.BASKET_LINK)

    def click_basket_link(self):
        self.browser.find_element(*self.BASKET_LINK).click()

    def search_button_should_be_present(self):
        return self.is_element_present(*self.SEARCH_BUTTON)
