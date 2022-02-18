import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math
from .base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//form[@id='add_to_basket_form']/button")
    PRODUCT_NAME_TITLE = (By.XPATH, "//div[@class='col-sm-6 product_main']/h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    PRODUCT_NAME_MESSAGE = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    BASKET_PRICE_MESSAGE = (By.XPATH, "//div[@id='messages']/div[3]/div/p/strong")
    PRODUCT_IMAGE = (By.XPATH, "//div[@class='image_container']/a/img")

    def get_product_price_value(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def get_product_name_value(self):
        return self.browser.find_element(*self.PRODUCT_NAME_TITLE).text

    def click_add_to_basket_button(self):
        self.browser.find_element(*self.ADD_TO_BASKET_BUTTON).click()
        return self.browser

    def click_product_image(self):
        self.browser.find_element(*self.PRODUCT_IMAGE).click()

    def solve_quiz_and_get_code(self):
        try:
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            time.sleep(1)
            alert.accept()
            time.sleep(1)

            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()

        except NoAlertPresentException:
            print("No second alert presented")

    def get_added_to_basket_product_name(self):
        base_page = BasePage(self.browser)
        return base_page.wait_until_element_present(*self.PRODUCT_NAME_MESSAGE)

    def get_added_to_basket_product_price(self):
        base_page = BasePage(self.browser)
        return base_page.wait_until_element_present(*self.BASKET_PRICE_MESSAGE)
