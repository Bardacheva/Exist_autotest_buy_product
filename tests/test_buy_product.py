import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.finish_page import Finish_page
# from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import Login_page

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pages.main_page import Main_page
from pages.payment_page import Payment_page

# @pytest.mark.order(3) # устанавливает очередность тестов
def test_buy_product_1(set_up, set_group):
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    print("Start Test 1")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_info_page(driver)
    cip.input_info()

    pay = Payment_page(driver)
    pay.payment()

    f = Finish_page(driver)
    f.finish()

    print("Finish Test 1")
    driver.quit()

# @pytest.mark.order(1) # устанавливает очередность тестов
def test_buy_product_2(set_up):
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    print("Start Test 2")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_2()

    cp = Cart_page(driver)
    cp.click_checkout_button()
    driver.quit()

    print("Finish Test 2")

# @pytest.mark.order(2) # устанавливает очередность тестов
def test_buy_product_3(set_up):
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    print("Start Test 3")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_3()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    print("Finish Test 3")
    driver.quit()

    # python -m pytest -s -v -k test_название_2 - запуск отдельного теста