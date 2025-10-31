import time
import allure
from urls import MAIN_URL
import locators
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from functions.functions import (
    generate_post_code,
    generate_first_name,
    generate_lastName,
    find_deleting_customer,
)


class Page(BasePage):

    @allure.step("Открываем главную страницу тестируемого приложения")
    def open_page(self):
        self.open(MAIN_URL)
        return self

    @allure.step("Добавление нового кастомера")
    def add_customer(self):

        with allure.step("Ищем кнопку 'Add Customer' и кликаем по ней"):
            button_add = self.wait_until_visible(locators.BUTTON_ADD_CUSTOMER)
            button_add.click()

        with allure.step("Генерируем PostCode, FirstName и LastName"):
            post_code = generate_post_code(10)
            first_name = generate_first_name(post_code)
            last_name = generate_lastName(first_name)

        with allure.step("Заполняем поля формы сгенерированными данными"):
            self.fill_input(locators.INPUT_FIRST_NAME, first_name)
            self.fill_input(locators.INPUT_LAST_NAME, last_name)
            self.fill_input(locators.INPUT_POST_CODE, post_code)

        with allure.step("Нажимаем кнопку подтверждения (Submit)"):
            button_submit = self.wait_until_visible(locators.BUTTON_SUBMIT_ADD_CUSTOMER)
            button_submit.click()

        time.sleep(5)
        return self

    @allure.step("Проверяем появление алерта с подтверждением добавления кастомера")
    def verify_add_customer_alert(self):
        alert = self.wait_for_alert()
        alert_text = "Customer added successfully with customer id :6"

        with allure.step("Сравниваем текст алерта с ожидаемым"):
            assert (
                alert.text == alert_text
            ), f"Ожидался '{alert_text}', а получили '{alert.text}'"

        alert.accept()
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
            except Exception as e:
                print(f"Ошибка при обработке строки: {e}")
                continue
        return first_names

    @allure.step(
        "Сортируем список кастомеров по имени и проверяем корректность сортировки"
    )
    def sort_and_check_customers(self):

        button_show_list_customers = self.wait_until_visible(
            locators.BUTTON_LIST_CUSTOMERS
        )
        button_show_list_customers.click()
        time.sleep(2)

        with allure.step("Получаем список имён до сортировки"):
            names_before_sorting = self.get_first_names()
            print("До сортировки:", names_before_sorting)

        with allure.step("Нажимаем на заголовок колонки 'First Name' для сортировки"):
            sort_by_fn = self.wait_until_visible(locators.SORT_BY_FIRST_NAME_HREF)
            sort_by_fn.click()
            time.sleep(2)

        with allure.step("Получаем список имён после сортировки"):
            names_after_sorting_desk = self.get_first_names()
            print("После сортировки:", names_after_sorting_desk)

        with allure.step("Проверяем корректность сортировки"):
            real_sort_desk = sorted(names_before_sorting, reverse=True)
            print("Целевой список:", real_sort_desk)
            assert (
                real_sort_desk == names_after_sorting_desk
            ), f"Ожидался {real_sort_desk}, а получили {names_after_sorting_desk}"

        time.sleep(5)
        return self

    @allure.step("Удаление кастомера по заданным требованиям")
    def delete_customer(self):
        with allure.step("Открываем список кастомеров"):
            button_show_list_customers = self.wait_until_visible(
                locators.BUTTON_LIST_CUSTOMERS
            )
            button_show_list_customers.click()
            time.sleep(2)

        customers = self.get_first_names()
        if not customers:
            print("Кастомеров нет, удалять нечего")
            return

        deleting_customer_name = find_deleting_customer(customers)
        print("Выбран для удаления:", deleting_customer_name)

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
            except Exception as e:
                print(f"Ошибка при обработке строки: {e}")
                continue

        # Проверяем, что кастомер удалён
        time.sleep(2)
        updated_customers = self.get_first_names()

        with allure.step("Проверяем, что кастомер действительно удалён"):
            assert (
                deleting_customer_name not in updated_customers
            ), f"Кастомер '{deleting_customer_name}' не был удалён"

        print("Удалено успешно.")
        return self
