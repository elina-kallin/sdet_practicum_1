from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(driver, 5)

    def open(self, url):
        self.driver.get(url)
        return self

    def inner_check_equals_url(self, url_reference):
        current_url = self.driver.current_url
        print("Статус правильности урла: ", current_url == url_reference)

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

    def fill_input(self, locator, keys):
        input_field = self.wait_until_visible(locator)
        input_field.click()
        input_field.clear()
        input_field.send_keys(keys)

    def wait_for_alert(self, timeout=5):
        wt = wait(self.driver, timeout)
        alert = wt.until(EC.alert_is_present())
        return alert

    def find_elements(self, parent):
        # elements = self.find_elements(*parent)
        # return elements
        return self.driver.find_elements(*parent)
