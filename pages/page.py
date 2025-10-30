import time
import allure
from constants import MAIN_URL
import locators
from pages.base_page import BasePage
from functions.functions import generate_post_code, generate_first_name


class Page(BasePage):

    def open_page(self):
        self.open(MAIN_URL)
        return self

    def add_customer(self):
        button_add = self.wait_until_visible(locators.BUTTON_ADD_CUSTOMER)
        button_add.click()

        input_post_code = self.wait_until_visible(locators.INPUT_POST_CODE)
        post_code = generate_post_code(10)
        input_post_code.click()
        input_post_code.clear()
        input_post_code.send_keys(post_code)

        input_first_name = self.wait_until_visible(locators.INPUT_FIRST_NAME)
        first_name = generate_first_name("7533887815")
        input_first_name.click()
        input_first_name.clear()
        input_first_name.send_keys(first_name)

        time.sleep(10)
