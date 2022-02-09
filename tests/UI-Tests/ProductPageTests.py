import pytest
import configparser
import time

from pages.product_page import ProductPage


class TestProductPage:
    config = configparser.ConfigParser()
    config.read('config.ini')
    url = config['URLs']['product_page']

    @pytest.mark.UI
    def test_add_product_to_basket(self, browser):
        product_page = ProductPage(browser)
        product_page.open(url=self.url)
        product_page.click_add_to_basket_button()
        time.sleep(5)
        product_page.solve_quiz_and_get_code()

