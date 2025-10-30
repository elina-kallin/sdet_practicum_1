import pytest
from selenium import webdriver as wb


@pytest.fixture(scope="function")
def browser():
    driver = wb.Firefox()
    yield driver
    driver.close()
