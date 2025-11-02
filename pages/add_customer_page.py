import allure
from urls import MAIN_URL
import locators
from pages.base_page import BasePage
from functions.functions import (
    generate_post_code,
    generate_first_name,
    generate_last_name,
)


class AddCustomerPage(BasePage):

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
            last_name = generate_last_name(first_name)

        with allure.step("Заполняем поля формы сгенерированными данными"):
            self.fill_input(locators.INPUT_FIRST_NAME, first_name)
            self.fill_input(locators.INPUT_LAST_NAME, last_name)
            self.fill_input(locators.INPUT_POST_CODE, post_code)

        with allure.step("Нажимаем кнопку подтверждения (Submit)"):
            button_submit = self.wait_until_visible(locators.BUTTON_SUBMIT_ADD_CUSTOMER)
            button_submit.click()

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
