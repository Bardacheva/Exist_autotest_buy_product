from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger
import allure

class Car_brand_page(Base):
# выбор марки автомобиля и года выпуска

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    suzuki = "//a[@href='/Catalog/Global/Cars/Suzuki']"  # car_brand_page
    year = "//div[@onclick='DDL.ToggleDropDown(this, event)']"  # car_brand_page
    choose_year = "//a[@href='/Catalog/Global/Cars/Suzuki?Year=2014']"  # car_brand_page


    # Getters

    def get_suzuki(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.suzuki)))

    def get_year(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.year)))

    def get_choose_year(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.choose_year)))


    # Actions

    def click_suzuki(self):
        self.get_suzuki().click()
        print("Click suzuki")

    def click_choose_year(self):
        self.get_choose_year().click()
        print("Click choose year")

    def click_year(self):
        self.get_year().click()
        print("Click year")


    # Methods

    def choose_brand(self):
        with allure.step("Choose_brand"):
            Logger.add_start_step(method="choose_brand")
            self.click_suzuki()
            self.click_year()
            self.click_choose_year()
            Logger.add_end_step(url=self.driver.current_url, method="choose_brand")
