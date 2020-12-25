from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BUTTON = (By.ID, "nav-signin-tooltip")
    CONTINUE_BUTTON = (By.ID, "continue")
    SIGN_IN_BUTTON = (By.ID, "signInSubmit")
    SEARCH_BUTTON_ICON = (By.ID, "nav-search-submit-text")
    NEXT_PAGE_BUTTON = (By.CLASS_NAME, "a-last")
    THIRD_ELEMENT = (By.XPATH, '//*[@data-cel-widget="search_result_2"]')
    ADD_TO_WISHLIST_BUTTON = (By.ID, "add-to-wishlist-button-submit")
    HOVER_ITEM = (By.CSS_SELECTOR, "#nav-flyout-wl-items > div > a > span")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".g-move-delete-buttons > span")
