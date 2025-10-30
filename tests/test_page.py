import pytest
from pages.page import Page as pg


def test_click_button(browser):
    page = pg(browser)
    (page.open_page().add_customer())
