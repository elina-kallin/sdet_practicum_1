import pytest
from pages.page import Page as pg


# def test_add_customer(browser):
#     page = pg(browser)
#     (page.open_page().add_customer().verify_add_customer_alert())


def test_sorting_customers_by_firstname(browser):
    page = pg(browser)
    (page.open_page().sort_and_check_customers())
