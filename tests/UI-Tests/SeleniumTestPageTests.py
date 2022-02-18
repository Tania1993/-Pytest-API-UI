import time

import pytest

from pages.base_page import BasePage
from pages.basket_page import BasketPage


@pytest.mark.UI
class TestSeleniumMainPage:

    def test_guest_should_see_login_link(self, browser):
        base_page = BasePage(browser)
        base_page.open()
        base_page.click_login_link()
        assert base_page.login_link_should_be_present(), 'Login link is not displayed'

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        base_page = BasePage(browser)
        base_page.open()
        assert base_page.basket_link_should_be_present(), 'Basket link is not displayed'

    @pytest.mark.xfail(reason='fixing')
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        base_page = BasePage(browser)
        base_page.open()
        assert base_page.search_button_should_be_present(), 'Search button is not displayed'

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        base_page = BasePage(browser)
        basket_page = BasketPage(browser)
        base_page.open()
        base_page.click_basket_link()
        assert basket_page.basket_is_empty_message_should_be_present(), 'Basket is not empty'
        assert basket_page.basket_items_should_not_be_displayed(), 'Basket is not empty'

