from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger
import allure

class Model_page(Base):
    # Выбор модели автомобиля

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    choose_model = "//a[@href='/Catalog/Global/Cars/Suzuki/26727']"


    # Getters

    def get_choose_model(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.choose_model)))


    # Actions

    def click_choose_model(self):
        self.get_choose_model().click()
        print("Click choose_model")


    # Methods

    def choose_models(self):
        with allure.step("Choose_models"):
            Logger.add_start_step(method="choose_models")
            self.get_current_url()
            self.driver.execute_script("window.scrollTo(0, 700)")
            self.click_choose_model()
            Logger.add_end_step(url=self.driver.current_url, method="choose_models")




