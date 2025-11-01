import allure
from pages.add_customer_page import AddCustomerPage as add_customer_page
from pages.customers_page import CustomersPage as customers_page


@allure.story("Добавление нового клиента")
@allure.title("Добавляем нового клиента и проверяем алерт")
def test_add_customer(browser):
    page = add_customer_page(browser)
    (page.open_page().add_customer().verify_add_customer_alert())


@allure.story("Сортировка клиентов по имени")
@allure.title("Проверяем корректность сортировки клиентов по First Name")
def test_sorting_customers_by_firstname(browser):
    page = customers_page(browser)
    (page.open_page().sort_and_check_customers())


@allure.story("Удаление клиента")
@allure.title("Удаляем клиента, ближайшего к среднему арифметическому по длине имени")
def test_deleting_customer(browser):
    page = customers_page(browser)
    (page.open_page().delete_and_check_deleting_customer())
