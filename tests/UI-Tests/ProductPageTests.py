from datetime import datetime
import pytest
import configparser

from pages.product_page import ProductPage
from pages.login_page import LoginPage

config = configparser.ConfigParser()
config.read('config.ini')


@pytest.mark.UI
class TestProductPage:
    product_page_with_bug = [f"{config['URLs']['product_page_with_bug']}?promo=offer{i}" for i in range(0, 10)]
    url = config['URLs']['product_page']

    def test_add_product_to_basket(self, browser):
        product_page = ProductPage(browser)
        product_page.open(url=self.url)
        product_page.click_login_link()
        login_page = LoginPage(browser)
        login_page.register(email=f'test_user_{str(datetime.today().strftime("%Y-%m-%d-%H%M%S"))}@fakemail.org', password='GoodPassword123456')
        product_page.click_product_image()
        product_page.click_add_to_basket_button()
        product_page.solve_quiz_and_get_code()

        assert product_page.get_added_to_basket_product_name().text == product_page.get_product_name_value()
        assert product_page.get_added_to_basket_product_price().text == product_page.get_product_price_value()

    @pytest.mark.UI2
    @pytest.mark.parametrize('urls', product_page_with_bug)
    @pytest.mark.xfail(reason='bugged link')
    def test_add_product_to_basket_with_bug(self, browser, urls):
        product_page = ProductPage(browser)
        product_page.open(url=urls)
        product_page.click_add_to_basket_button()

    def test_guest_user_should_see_login_link(self, browser):
        product_page = ProductPage(browser)
        product_page.open(self.url)
        assert product_page.login_link_should_be_present(), 'Login link is not displayed'

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        product_page = ProductPage(browser)
        product_page.open(self.url)
        product_page.click_login_link()
        login_page = LoginPage(browser)
        assert login_page.page_should_be_opened('login'), 'Login page is not opened'
