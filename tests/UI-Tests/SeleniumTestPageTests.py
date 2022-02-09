import pytest

from pages.main_page import MainPage


class TestSeleniumMainPage:

    @pytest.mark.UI
    def test_guest_should_see_login_link(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.click_login_link()
        main_page.login_link_should_be_present()

    @pytest.mark.UI
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.basket_link_should_be_present()

    @pytest.mark.xfail(reason='fixing')
    @pytest.mark.UI
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        main_page = MainPage(browser)
        main_page.open()
        main_page.search_button_should_be_present()
