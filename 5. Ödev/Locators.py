from selenium.webdriver.common.by import By

utmSettings = (
    By.CSS_SELECTOR, ".utmSettings > div >p")  # 1.utmSettings for whole div, css selector for clickable element
inputWarningMessage = (By.CSS_SELECTOR, ".smsMessage > fieldset > p")  # 2
JourneyListFilterInput = (By.ID, "search-value")  # 3
TestRadioButton = (By.ID, "Test")  # 4 input might be not enough but if we try to take label, things get ugly.
STATISTICS = (By.PARTIAL_LINK_TEXT, "/journey-builder/121909/statistics")  # 5
removeVariationIcon = (By.ID, "delete")  # 6
CHANGE_ELEMENT = (By.PARTIAL_LINK_TEXT, "/assets/img/journey-builder/do-it-your-self/change.svg")  # 7
REMOVE_ELEMENT = (By.PARTIAL_LINK_TEXT, "/assets/img/journey-builder/do-it-your")
alertPanel = (By.CLASS_NAME, 'messageAlertBoxIcon')  # 8
createPersonalization = (By.CLASS_NAME, "btnBlue")  # 9
