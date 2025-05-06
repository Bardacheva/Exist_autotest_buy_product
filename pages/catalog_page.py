from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    catalog = "//a[@href='/Catalog/Global/Cars/Suzuki/26727/36C00078']" # catalog_page
    bodywork = "//div[@data-id='100']" # catalog_page
    piston = "//a[@href='/Catalogs/Global/Parts?i=36C00078&id=12C00000_9191']" # catalog_page
    search = "//a[@class='search-btn']" # catalog_page




    # Getters


    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_bodywork(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.bodywork)))

    def get_piston(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.piston)))

    def get_search(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.search)))




    # Actions


    def click_catalog(self):
        self.get_catalog().click()
        print("Click catalog")

    def click_bodywork(self):
        self.get_bodywork().click()
        print("Click bodywork")

    def click_piston(self):
        self.get_piston().click()
        print("Click piston")

    def click_search(self):
        self.get_search().click()
        print("Click search")




    # Methods

    def select_products(self):
        self.get_current_url()

        self.click_catalog()
        self.click_bodywork()
        self.click_piston()
        self.click_search()




