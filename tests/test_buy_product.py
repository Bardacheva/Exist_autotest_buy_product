import time
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pages.car_brand_page import Car_brand_page
from pages.cart_page import Cart_page
from pages.price_page import Price_page
from pages.model_page import Model_page
from pages.modification_page import Modification_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.catalog_page import Catalog_page

@allure.description("Test buy product")
def test_buy_product(set_up):

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    print("Start Test")

    login = Login_page(driver)
    login.authorization()

    cbp = Car_brand_page(driver)
    cbp.choose_brand()

    model_page = Model_page(driver)
    model_page.choose_models()

    modif_page = Modification_page(driver)
    modif_page.select_modification()

    catalog_page = Catalog_page(driver)
    catalog_page.choose_product()

    pp = Price_page(driver)
    pp.select_products()

    cart_page = Cart_page(driver)
    cart_page.product_confirmation()

    f = Finish_page(driver)
    f.finish()

    print("Finish Test")
    driver.quit()
