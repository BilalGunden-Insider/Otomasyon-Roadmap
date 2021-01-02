from selenium import webdriver
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# https://www.spx.com.tr/ adresine gidin.
# Herhangi bir kategori sayfasına gidin.
# Herhangi bir ürün sayfasına gidin.
# Ürünü sepete ekleyin.
# Sepet sayfasına gidin.
# Anasayfaya geri dönün.

class Test(unittest.TestCase):

    def basicSelenium(self):
        browser = webdriver.Chrome('C:\webdriver\chromedriver.exe')
        wait = WebDriverWait(browser, 10)

        MANCATEGORY = (By.CSS_SELECTOR, ".sub-menu:nth-child(2)")
        FIRSTITEM = (By.CLASS_NAME, "ems-prd-inner")
        SIZESELECTBUTTON = (By.CSS_SELECTOR, ".dropdownrow:nth-child(1)")
        ADDTOCARTBUTTON = (By.CLASS_NAME, "urunDetay_btnSepeteAt")
        SELECTCART = (By.CLASS_NAME, "ems-clone-mini-quatity")
        GOTOCART = (By.ID, "plhKSepet_sepetLink")
        BACKTOHOMEPAGEBUTTON = (By.CLASS_NAME, "sepetLogo")
        CATEGORYASSERTTEXTLOC = (By.CLASS_NAME, "navigasyonSeviye1")
        PRODUCTASSERTTEXTLOC = (By.CLASS_NAME, "ems-prd-name")
        PRODUCTTEXTLOC = (By.CLASS_NAME, "emos_H1")
        CARTPAGEASSERTIONTEXT = (By.CLASS_NAME, "btnSiparisTamamla")
        browser.get("https://www.spx.com.tr/")  # Go to website
        browser.maximize_window()  # maximize window to prevent possible responsiveness issues

        wait.until(EC.presence_of_element_located(MANCATEGORY)).click()  # go to category page

        categoryAssertText = wait.until(EC.presence_of_element_located(
            CATEGORYASSERTTEXTLOC)).text.upper()  # assert you move to first category page. In this case its ERKEK
        self.assertEqual(categoryAssertText, "ERKEK")

        productAssertText = wait.until(EC.presence_of_element_located(
            PRODUCTASSERTTEXTLOC)).text  # get product name from category page for assertion
        wait.until(EC.presence_of_element_located(FIRSTITEM)).click()  # Go to product page
        productText = wait.until(EC.presence_of_element_located(
            PRODUCTTEXTLOC)).text  # get product name from product page for assertion
        self.assertEqual(productText, productAssertText)  # Assert two text

        wait.until(EC.presence_of_element_located(SIZESELECTBUTTON)).click()  # select size

        wait.until(EC.presence_of_element_located(ADDTOCARTBUTTON)).click()  # add to cart

        browser.refresh()  # refresh page to prevent pop-up and possible coupon adds

        wait.until(EC.presence_of_element_located(SELECTCART)).click()  # click cart button for preparing go to cartpage

        wait.until(EC.element_to_be_clickable(GOTOCART)).click()  # go to cart page

        cartPageAssertionText = wait.until(EC.presence_of_element_located(
            CARTPAGEASSERTIONTEXT)).text  # asserting we are in cart page
        self.assertEqual(cartPageAssertionText, "Siparişi Tamamla")

        wait.until(EC.presence_of_element_located(BACKTOHOMEPAGEBUTTON)).click()  # go back to main page

        browser.quit()  # end test


test1 = Test()
test1.basicSelenium()
