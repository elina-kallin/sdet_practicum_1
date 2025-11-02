import allure
from urls import MAIN_URL
import locators
from pages.base_page import BasePage
from functions.functions import find_deleting_customer
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
)


class CustomersPage(BasePage):

    @allure.step("Открываем главную страницу тестируемого приложения")
    def open_page(self):
        self.open(MAIN_URL)
        return self

    @allure.step("Открытие списка кастомеров")
    def button_customers_click(self):
        self.wait_until_visible(locators.BUTTON_LIST_CUSTOMERS).click()
        return self

    @allure.step("Выгружаем список кастомеров")
    def get_first_names(self):
        first_names = []
        # Получаем все строки в теле таблицы
        tbody = self.wait_until_visible(locators.TBODY)
        rows = tbody.find_elements(*locators.TR)
        for row in rows:
            try:
                # Запихиваем в массив тексты первых ячеек каждой строки
                first_td = row.find_element(*locators.FIRST_CELL_IN_ROW)
                text = first_td.text.strip()
                if text:
                    first_names.append(text)
            except (NoSuchElementException, StaleElementReferenceException):
                continue
        return first_names

    @allure.step("Выполняем сортировку кастомеров по имени")
    def sort_customers_by_first_name(self):
        self.button_customers_click()

        sort_by_fn = self.wait_until_visible(locators.SORT_BY_FIRST_NAME_HREF)
        sort_by_fn.click()

        return self

    @allure.step("Проверяем корректность сортировки")
    def check_sorting(self, names_before, names_after):
        expected_sorted_names = sorted(names_before, reverse=True)
        assert (
            expected_sorted_names == names_after
        ), f"Ожидался {expected_sorted_names}, а получили {names_after}"
        return self

    @allure.step("Общий метод для сортировки и проверки")
    def sort_and_check_customers(self):
        self.button_customers_click()
        names_before = self.get_first_names()
        self.sort_customers_by_first_name()
        names_after = self.get_first_names()
        self.check_sorting(names_before, names_after)
        return self

    @allure.step("Удаление кастомера по заданным требованиям")
    def delete_customer(self):
        with allure.step("Открываем список кастомеров"):
            self.button_customers_click()

        customers = self.get_first_names()
        if not customers:
            return

        deleting_customer_name = find_deleting_customer(customers)

        tbody = self.wait_until_visible(locators.TBODY)
        rows = tbody.find_elements(*locators.TR)

        # Ищем строку с нужным именем
        for row in rows:
            try:
                first_td = row.find_element(*locators.FIRST_CELL_IN_ROW)
                if first_td.text.strip() == deleting_customer_name:
                    with allure.step(f"Удаляем кастомера '{deleting_customer_name}'"):
                        delete_button = row.find_element(
                            *locators.BUTTON_DELETE_CUSTOMER
                        )
                        delete_button.click()
                        break
            except (NoSuchElementException, StaleElementReferenceException):
                continue

        return deleting_customer_name

    @allure.step("Проверка отсутствия удаленного кастомера")
    def check_deleting_customer(self, deleted_customer_name):

        customers_after = self.get_first_names()

        with allure.step("Проверяем, что кастомер действительно удалён"):
            assert (
                deleted_customer_name not in customers_after
            ), f"Кастомер '{deleted_customer_name}' не был удалён"
        return self

    @allure.step("Удаляем и проверяем удаление")
    def delete_and_check_deleting_customer(self):
        deleted_customer_name = self.delete_customer()

        if deleted_customer_name:
            self.check_deleting_customer(deleted_customer_name)

        return self
