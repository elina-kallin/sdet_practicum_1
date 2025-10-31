from selenium.webdriver.common.by import By

BUTTON_ADD_CUSTOMER = (By.CSS_SELECTOR, 'button[ng-click="addCust()"]')
INPUT_POST_CODE = (By.CSS_SELECTOR, 'input[placeholder="Post Code"]')
INPUT_FIRST_NAME = (By.CSS_SELECTOR, 'input[placeholder="First Name"]')
INPUT_LAST_NAME = (By.CSS_SELECTOR, 'input[placeholder="Last Name"]')
BUTTON_SUBMIT_ADD_CUSTOMER = (By.CSS_SELECTOR, 'button[type="submit"]')

BUTTON_LIST_CUSTOMERS = (By.CSS_SELECTOR, 'button[ng-click="showCust()"]')
SORT_BY_FIRST_NAME_HREF = (
    By.XPATH,
    "/html/body/div/div/div[2]/div/div[2]/div/div/table/thead/tr/td[1]/a",
)

PARENT_COLUMN_FOR_SORT_FIRST_NAME = (
    By.XPATH,
    "/html/body/div/div/div[2]/div/div[2]/div/div/table/tbody/tr",
)

TR = (By.CSS_SELECTOR, "tr")
TBODY = (
    By.TAG_NAME,
    "tbody",
)
FIRST_CELL_IN_ROW = (By.XPATH, "./td[1]")
BUTTON_DELETE_CUSTOMER = (By.CSS_SELECTOR, 'button[ng-click="deleteCust(cust)"]')
