import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.price_page import Price_page
from utilities.logger import Logger
import allure

class Finish_page(Base):
    # Работа на финальной странице

    description_from_finish = ''
    sum_from_finish = ''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    check_sum_from_finish = "//span[@class='summa all']" # получаем стоимость со страницы
    check_description_from_finish = "//div[@class='prc-table__description']" # получаем название со страницы

    # Getters
    def get_main_word_from_finish(self): # получаем название товара с финальной страницы для проверки
        description_from_finish = (WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_description_from_finish))))
        Finish_page.description_from_finish = description_from_finish.text
        print(f"Товар на финальной странице: {Finish_page.description_from_finish}")
        return Finish_page.description_from_finish


    def get_sum_from_finish(self): # получаем стоимость товара с финальной страницы для проверки
        sum_from_finish = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.check_sum_from_finish)))
        Finish_page.sum_from_finish = sum_from_finish.text
        print(f"Стоимость товара на финальной странице: {Finish_page.sum_from_finish}")
        return Finish_page.sum_from_finish

    # Actions

    # Methods

    def finish(self):
        with allure.step("Finish"):
            Logger.add_start_step(method="finish")
            self.get_current_url()
            self.assert_url("https://exist.ru/Profile/Orders/CheckOrder.aspx?ofid=730")
            self.get_main_word_from_finish()
            self.get_sum_from_finish()
            self.assert_word(Finish_page.description_from_finish, Price_page.description_from_pp) # проверяем, идентично ли название товара
            self.assert_word(Finish_page.sum_from_finish, Price_page.sum_from_pp) # проверяем, идентична ли стоимость товара
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="finish")
