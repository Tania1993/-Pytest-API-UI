import pytest
import configparser


#@pytest.mark.parametrize('language', ['en-gb', 'ru'])
class TestSeleniumMainPage:
    config = configparser.ConfigParser()
    config.read('config.ini')
    link = config['URLs']['selenium_test_page']

    @pytest.mark.UI
    def test_guest_should_see_login_link(self, browser):
        browser.get(f'{self.link}/')
        browser.find_element_by_css_selector('#login_link')

    @pytest.mark.UI
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(f'{self.link}/')
        browser.find_element_by_css_selector('.basket-mini .btn-group > a')

    @pytest.mark.xfail(reason='fixing')
    @pytest.mark.UI
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(f'{self.link}/')
        browser.find_element_by_css_selector('button.favorite')
