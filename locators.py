from selenium.webdriver.common.by import By

BUTTON_ADD_CUSTOMER = (By.CSS_SELECTOR, 'button[ng-click="addCust()"]')
INPUT_POST_CODE = (By.CSS_SELECTOR, 'input[placeholder="Post Code"]')
INPUT_FIRST_NAME = (By.CSS_SELECTOR, 'input[placeholder="First Name"]')
INPUT_LAST_NAME = (By.CSS_SELECTOR, 'input[placeholder="Last Name"]')
BUTTON_SUBMIT_ADD_CUSTOMER = (By.CSS_SELECTOR, 'button[type="submit"]')

BUTTON_LIST_CUSTOMERS = (By.CSS_SELECTOR, 'button[ng-click="showCust()"]')
SORT_BY_FIRST_NAME_HREF = (
    By.CSS_SELECTOR,
    "a[ng-click=\"sortType = 'fName'; sortReverse = !sortReverse\"]",
)

TR = (By.CSS_SELECTOR, "tr")
TBODY = (
    By.TAG_NAME,
    "tbody",
)
FIRST_CELL_IN_ROW = (By.XPATH, "./td[1]")
BUTTON_DELETE_CUSTOMER = (By.CSS_SELECTOR, 'button[ng-click="deleteCust(cust)"]')
