from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger
import allure


class Price_page(Base):

    description_from_pp = ''
    sum_from_pp = ''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    select_product = "//a[@id='_79311240_0100da0234076c3105b6952e0100c0ad_730_29']"
    check_sum = "(//span[@class='price'])[3]" # получаем стоимость со страницы
    check_description = "(//a[@href='/Parts.axd?pid=79311240&flag=1064992'])[1]" # получаем название со страницы

    # Getters


    def get_select_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product)))

    def get_main_word_from_price_page(self):
        description_from_price_page = (WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_description))))
        Price_page.description_from_pp = description_from_price_page.text
        print(f"Выбранный товар: {Price_page.description_from_pp}")
        return Price_page.description_from_pp

    def get_sum_from_price_page(self):
        sum_from_price_page = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_sum)))
        Price_page.sum_from_pp = sum_from_price_page.text
        print(f"Стоимость выбранного товара: {Price_page.sum_from_pp}")
        return Price_page.sum_from_pp


    # Actions

    def click_select_product(self):
        self.get_select_product().click()
        print("Click select product")


    # Methods

    def select_products(self):
        with allure.step("Select_products"):
            Logger.add_start_step(method="select_products")
            self.get_current_url()
            self.click_select_product()
            self.get_main_word_from_price_page()
            self.get_sum_from_price_page()
            self.assert_word(Price_page.description_from_pp, 'Пистон, облицовка днища кузова "Febi Plus"')  # проверяем, идентично ли название товара
            self.assert_word(Price_page.sum_from_pp, '613 ₽')  # проверяем, идентична ли стоимость товара
            Logger.add_end_step(url=self.driver.current_url, method="select_products")