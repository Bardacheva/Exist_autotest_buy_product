from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger
import allure

class Modification_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    modification = "//a[@href='/Catalog/Global/Cars/Suzuki/26727/36C00078/?r=1']"


    # Getters

    def get_modification(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.modification)))


    # Actions

    def click_modification(self):
        self.get_modification().click()
        print("Click modification")


    # Methods

    def select_modification(self):
        with allure.step("Select_modification"):
            Logger.add_start_step(method="select_modification")
            self.get_current_url()
            self.click_modification()
            Logger.add_end_step(url=self.driver.current_url, method="select_modification")




