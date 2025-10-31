import allure
from pages.page import Page as pg


@allure.story("Добавление нового клиента")
@allure.title("Добавляем нового клиента и проверяем алерт")
def test_add_customer(browser):
    page = pg(browser)
    (page.open_page().add_customer().verify_add_customer_alert())


@allure.story("Сортировка клиентов по имени")
@allure.title("Проверяем корректность сортировки клиентов по First Name")
def test_sorting_customers_by_firstname(browser):
    page = pg(browser)
    (page.open_page().sort_and_check_customers())


@allure.story("Удаление клиента")
@allure.title("Удаляем клиента, ближайшего к среднему арифметическому по длине имени")
def test_deleting_customer(browser):
    page = pg(browser)
    (page.open_page().delete_customer())
