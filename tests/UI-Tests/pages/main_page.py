from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    LOGIN_LINK_CSS_SELECTOR = (By.CSS_SELECTOR, '#login_link')
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini .btn-group > a')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button.favorite')

    def click_login_link(self):
        login_link = self.browser.find_element(*self.LOGIN_LINK_CSS_SELECTOR)
        login_link.click()

    def login_link_should_be_present(self):
        assert self.is_element_present(*self.LOGIN_LINK_CSS_SELECTOR), 'Login link is not presented'

    def basket_link_should_be_present(self):
        assert self.is_element_present(*self.BASKET_LINK), 'Basket link is not displayed'

    def search_button_should_be_present(self):
        assert self.is_element_present(*self.SEARCH_BUTTON), 'Search button is not displayed'
