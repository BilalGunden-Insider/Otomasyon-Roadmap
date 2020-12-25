from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locators
from selenium.webdriver.common.action_chains import ActionChains
import unittest


class amazonFunctions(unittest.TestCase):
    def __init__(self, browser):
        super().__init__()
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def login(self, email, password):
        self.wait.until(EC.presence_of_element_located(Locators.LOGIN_BUTTON)).click()
        self.browser.find_element_by_id("ap_email").send_keys(email)
        self.wait.until(EC.presence_of_element_located(Locators.CONTINUE_BUTTON)).click()
        self.browser.find_element_by_id("ap_password").send_keys(password)
        self.wait.until(EC.presence_of_element_located(Locators.SIGN_IN_BUTTON)).click()

    def elemStringAssertion(self, Locator, String):
        assertion_text = self.wait.until(EC.presence_of_element_located(Locator)).text
        self.assertEqual(assertion_text, String)

    def searchKey(self, Key):
        self.browser.find_element_by_id("twotabsearchtextbox").send_keys(Key)
        self.wait.until(EC.presence_of_element_located(Locators.SEARCH_BUTTON_ICON)).click()
        searched_input = self.wait.until(EC.presence_of_element_located("a-color-state")).text
        self.assertEqual(searched_input, '"' + Key + '"')

    def hoverClick(self, hoverLocator, clickLocator):
        hoverable_item = self.browser.find_element_by_id(hoverLocator)
        hover = ActionChains(self.browser).move_to_element(hoverable_item)
        hover.perform()
        self.wait.until(EC.element_to_be_clickable(clickLocator)).click()
