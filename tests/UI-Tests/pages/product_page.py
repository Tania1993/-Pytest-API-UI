from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math
from .base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_INFO_CONTAINER = (By.XPATH, '//div[class="col-sm-6 product_main"]')
    ADD_TO_BASKET_BUTTON = (By.XPATH, f'{PRODUCT_INFO_CONTAINER}/form/button')
    PRODUCT_NAME_TITLE = (By.XPATH, f'{PRODUCT_INFO_CONTAINER}/h1')
    PRODUCT_PRICE = (By.XPATH, f'{PRODUCT_INFO_CONTAINER}/p[class="price_color"]')

    def get_product_price_value(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def get_product_name_value(self):
        return self.browser.find_element(*self.PRODUCT_NAME_TITLE).text

    def click_add_to_basket_button(self):
        self.browser.find_element(self.ADD_TO_BASKET_BUTTON).click()
        return self.browser

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f'Your code: {alert_text}')
            alert.accept()
        except NoAlertPresentException:
            print('No second alert presented')
