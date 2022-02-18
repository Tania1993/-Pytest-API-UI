from selenium.webdriver.common.by import By

from .base_page import BasePage


class BasketPage(BasePage):
    BASKET_IS_EMPTY_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p[contains(text(), 'empty')]")
    BASKET_ITEMS = (By.CSS_SELECTOR, "basket-items")

    def basket_is_empty_message_should_be_present(self):
        base_page = BasePage(self.browser)
        return base_page.is_element_present(*self.BASKET_IS_EMPTY_MESSAGE)

    def get_basket_items(self):
        return self.browser.find_element(*self.BASKET_ITEMS)

    def basket_items_should_not_be_displayed(self):
        base_page = BasePage(self.browser)
        return base_page.is_not_element_present(*self.BASKET_ITEMS)