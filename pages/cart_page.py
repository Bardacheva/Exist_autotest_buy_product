from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pages
from base.base_class import Base
from pages.price_page import Price_page
from utilities.logger import Logger
import allure

class Cart_page(Base):
    # Работа с корзиной

    description_from_cart = ''
    sum_from_cart = ''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    cart = "//a[@class='shop-functions__cart js-cartfull']"  # cart_page
    continue_registration = "//a[@id='ctl00_ctl00_b_b_repOffices_ctl00_slbInvokeSubmit']"
    check_sum_from_cart = "(//div[@class='prc-table__sumprice'])[2]" # получаем стоимость со страницы
    check_description_from_cart = "//div[@class='prc-table__description']" # получаем название со страницы

    # Getters

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_main_word_from_cart(self):
        description_from_cart = (WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_description_from_cart))))
        Cart_page.description_from_cart = description_from_cart.text
        print(f"Товар в корзине: {Cart_page.description_from_cart}")
        return Cart_page.description_from_cart


    def get_sum_from_cart(self):
        sum_from_cart = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_sum_from_cart)))
        Cart_page.sum_from_cart = sum_from_cart.text
        print(f"Стоимость товара в корзине: {Cart_page.sum_from_cart}")
        return Cart_page.sum_from_cart

    def get_continue_registration(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_registration)))



    # Actions

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_continue_registration(self):
        self.get_continue_registration().click()
        print("Click continue_registration")


    # Methods

    def product_confirmation(self):
        with allure.step("Product_confirmation"):
            Logger.add_start_step(method="product_confirmation")
            self.click_cart()
            self.get_main_word_from_cart()
            self.get_sum_from_cart()
            self.assert_word(Cart_page.description_from_cart, Price_page.description_from_pp) # проверяем, идентично ли название товара
            self.assert_word(Cart_page.sum_from_cart, Price_page.sum_from_pp) # проверяем, идентична ли стоимость товара
            self.click_continue_registration()
            Logger.add_end_step(url=self.driver.current_url, method="product_confirmation")

