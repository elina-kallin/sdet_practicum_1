import time
import allure
from constants import MAIN_URL
import locators
from pages.base_page import BasePage
from functions.functions import (
    generate_post_code,
    generate_first_name,
    generate_lastName,
)


class Page(BasePage):

    def open_page(self):
        self.open(MAIN_URL)
        return self

    def add_customer(self):
        button_add = self.wait_until_visible(locators.BUTTON_ADD_CUSTOMER)
        button_add.click()

        post_code = generate_post_code(10)
        first_name = generate_first_name(post_code)
        last_name = generate_lastName(first_name)

        self.fill_input(locators.INPUT_POST_CODE, post_code)
        self.fill_input(locators.INPUT_FIRST_NAME, first_name)
        self.fill_input(locators.INPUT_LAST_NAME, last_name)

        button_submit = self.wait_until_visible(locators.BUTTON_SUBMIT_ADD_CUSTOMER)
        button_submit.click()

        time.sleep(5)

        return self

    def verify_add_customer_alert(self):
        alert = self.wait_for_alert()
        alert_text = "Customer added successfully with customer id :6"

        assert (
            alert.text == alert_text
        ), f"Ожидался {alert_text}, а получили {alert.text}"

        alert.accept()
        return self
