import pytest
from selenium import webdriver as wb
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="module")
def browser():
    options = Options()
    options.add_argument("--headless")
    driver = wb.Firefox(options=options)
    yield driver
    driver.quit()
