import time

import pytest
import configparser

from pages.product_page import ProductPage

config = configparser.ConfigParser()
config.read('config.ini')


class TestProductPage:
    product_page_with_bug = [f"{config['URLs']['product_page_with_bug']}?promo=offer{i}" for i in range(0, 10)]

    @pytest.mark.UI
    def test_add_product_to_basket(self, browser):
        url = config['URLs']['product_page']
        product_page = ProductPage(browser)
        product_page.open(url=url)
        product_page.click_add_to_basket_button()
        product_page.solve_quiz_and_get_code()

        assert product_page.get_added_to_basket_product_name().text == product_page.get_product_name_value()
        assert product_page.get_added_to_basket_product_price().text == product_page.get_product_price_value()

    @pytest.mark.UI
    @pytest.mark.parametrize('urls', product_page_with_bug)
    @pytest.mark.xfail(reason='bugged link')
    def test_add_product_to_basket_with_bug(self, browser, urls):
        product_page = ProductPage(browser)
        product_page.open(url=urls)
        product_page.click_add_to_basket_button()

        #time.sleep(2)
