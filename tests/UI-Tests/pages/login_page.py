import time

from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    LOGIN_SECTION = ()
    EMAIL_FIELD = ()
    PASSWORD_FIELD = ()
    LOGIN_BUTTON = ()
    REGISTER_SECTION = ()
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

    def enter_email(self, email):
        email_field = self.browser.find_element(*self.REGISTRATION_EMAIL)
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.browser.find_element(*self.REGISTRATION_PASSWORD)
        password_field.send_keys(password)

    def enter_confirm_password(self, password):
        confirm_password_field = self.browser.find_element(*self.REGISTRATION_CONFIRM_PASSWORD)
        confirm_password_field.send_keys(password)

    def click_register_button(self):
        self.browser.find_element(*self.REGISTER_BUTTON).click()

    def register(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.click_register_button()
        self.wait_until_element_present(*self.USER_ICON)
