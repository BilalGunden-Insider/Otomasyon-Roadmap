from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator import Locators
from functions import amazonFunctions


class Test(unittest.TestCase):
    def wholeProject(self):
        browser = webdriver.Chrome('C:\webdriver\chromedriver.exe')
        wait = WebDriverWait(browser, 10)
        browser.get("http://www.amazon.com.tr")
        browser.maximize_window()
        amazonFunction = amazonFunctions(browser)
        amazonFunction.elemStringAssertion("nav-line-1-container", "Merhaba, Giriş yap")
        amazonFunction.login('mail yazılacak', 'password yazılacak')
        amazonFunction.searchKey("Samsung")
        wait.until(EC.presence_of_element_located(Locators.NEXT_PAGE_BUTTON)).click()
        time.sleep(1)
        amazonFunction.elemStringAssertion("a-selected", "2")
        time.sleep(1)
        wait.until(EC.presence_of_element_located(Locators.THIRD_ELEMENT)).click()
        wait.until(EC.presence_of_element_located(Locators.ADD_TO_WISHLIST_BUTTON)).click()
        browser.refresh()
        product_name_text = browser.find_element_by_class_name("product-title-word-break").text
        amazonFunction.hoverClick("nav-link-accountList", Locators.HOVER_ITEM)
        product_name_assertion_text = browser.find_element_by_css_selector(".a-row .a-size-small > h3").text
        self.assertEqual(product_name_text, product_name_assertion_text)
        wait.until(EC.presence_of_element_located(Locators.DELETE_BUTTON)).click()
        browser.refresh()
        amazonFunction.elemStringAssertion("no-items-section", "Bu listede 0 ürün var")
        browser.quit()


testObject = Test()
testObject.wholeProject()
