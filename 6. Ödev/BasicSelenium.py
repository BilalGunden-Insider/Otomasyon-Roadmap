from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test(unittest.TestCase):

    def basicSelenium(self):
        browser = webdriver.Chrome('C:\webdriver\chromedriver.exe')
        wait = WebDriverWait(browser, 10)

        manCategory = (By.CSS_SELECTOR, ".sub-menu:nth-child(2)")
        FirstItem = (By.CLASS_NAME, "ems-prd-inner")
        sizeSelectButton = (By.CSS_SELECTOR, ".dropdownrow:nth-child(1)")
        addToCartButton = (By.CLASS_NAME, "urunDetay_btnSepeteAt")
        selectCart = (By.CLASS_NAME, "ems-clone-mini-quatity")
        goToCart = (By.ID, "plhKSepet_sepetLink")
        backToHomepageButton = (By.CLASS_NAME, "sepetLogo")

        browser.get("https://www.spx.com.tr/")  # Go to website
        browser.maximize_window()  # maximize window to prevent possible responsiveness issues

        wait.until(EC.presence_of_element_located(manCategory)).click()  # go to category page

        categoryAssertText = browser.find_element_by_class_name(
            "navigasyonSeviye1").text.upper()  # assert you move to first category page. In this case its ERKEK
        self.assertEqual(categoryAssertText, "ERKEK")
        
        productAssertText = browser.find_element_by_class_name(
            "ems-prd-name").text  # get product name from category page for assertion
        wait.until(EC.presence_of_element_located(FirstItem)).click()  # Go to product page
        productText = browser.find_element_by_class_name(
            "emos_H1").text  # get product name from product page for assertion
        self.assertEqual(productText, productAssertText)  # Assert two text

        wait.until(EC.presence_of_element_located(sizeSelectButton)).click()  # select size

        wait.until(EC.presence_of_element_located(addToCartButton)).click()  # add to cart

        browser.refresh()  # refresh page to prevent pop-up and possible coupon adds

        wait.until(EC.presence_of_element_located(selectCart)).click()  # click cart button for preparing go to cartpage

        wait.until(EC.element_to_be_clickable(goToCart)).click()  # go to cart page

        cartPageAssertionText = browser.find_element_by_class_name(
            "btnSiparisTamamla").text  # asserting we are in cart page
        self.assertEqual(cartPageAssertionText, "Siparişi Tamamla")

        wait.until(EC.presence_of_element_located(backToHomepageButton)).click()  # go back to main page

        browser.quit()  # end test


test1 = Test()
test1.basicSelenium()
