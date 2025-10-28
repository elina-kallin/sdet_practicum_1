from constants import MAIN_URL
import locators
from pages.base_page import BasePage


class Page(BasePage):

    def openPage(self):
        self.open(MAIN_URL)
        return self

    def add_customer(self):
        button_add = self.wait_until_visible(
            self.findElement(locators.BUTTON_ADD_CUSTOMER)
        )
        button_add.click()
