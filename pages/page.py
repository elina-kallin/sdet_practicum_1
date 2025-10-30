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

    def get_first_names(self):
        first_names = self.find_elements(locators.PARENT_COLUMN_FOR_SORT_FIRST_NAME)
        return [fn.text.strip() for fn in first_names if fn.text.strip()]

    def sort_and_check_customers(self):
        button_show_list_customers = self.wait_until_visible(
            locators.BUTTON_LIST_CUSTOMERS
        )
        button_show_list_customers.click()
        time.sleep(2)

        names_before_sorting = self.get_first_names()
        print("До сортировки: ", names_before_sorting)

        sort_by_fn = self.wait_until_visible(locators.SORT_BY_FIRST_NAME_HREF)
        sort_by_fn.click()
        time.sleep(2)

        names_after_sorting_desk = self.get_first_names()
        print("После сортировки: ", names_after_sorting_desk)

        real_sort_desk = sorted(names_before_sorting, reverse=True)
        print("Целевой список: ", real_sort_desk)

        assert (
            real_sort_desk == names_after_sorting_desk
        ), f"Ожидался список {real_sort_desk}, а получилась фигня: {names_after_sorting_desk}"

        time.sleep(5)
        return self
