import configparser


class TestSeleniumMainPage:
    # вызываем фикстуру в тесте, передав ее как параметр
    config = configparser.ConfigParser()
    link = config["URLs"]["selenium_test_page"]

    def test_guest_should_see_login_link(self, browser):
        browser.get(self.link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(self.link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")