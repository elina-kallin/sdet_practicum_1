from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(driver, 5)

    def open(self, url):
        self.driver.get(url)
        return self

    def findElement(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return self

    def wait_until_visible(self, locator, timeout=10):
        return wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_until_clicable(self, locator, timeout=10):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
