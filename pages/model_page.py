from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    choose_model = "//a[@href='/Catalog/Global/Cars/Suzuki/26727']" # model_page
    modification = "//a[@href='/Catalog/Global/Cars/Suzuki/26727/36C00078/?r=1']" # modification_page
    catalog = "//a[@href='/Catalog/Global/Cars/Suzuki/26727/36C00078']" # catalog_page
    bodywork = "//div[@data-id='100']" # catalog_page
    piston = "//a[@href='/Catalogs/Global/Parts?i=36C00078&id=12C00000_9191']" # catalog_page
    search = "//a[@class='search-btn']" # catalog_page
    select_product = "//a[@id='_79311240_0100da0234076c3105b6952e0100c0ad_730_29']" # price_page



    # Getters



    def get_choose_model(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.choose_model)))

    def get_modification(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.modification)))

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

    def get_select_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product)))



    # Actions



    def click_choose_model(self):
        self.get_choose_model().click()
        print("Click choose_model")

    def click_modification(self):
        self.get_modification().click()
        print("Click modification")

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

    def click_select_product(self):
        self.get_select_product().click()
        print("Click select product")



    # Methods

    def select_products(self):
        self.get_current_url()

        self.driver.execute_script("window.scrollTo(0, 700)")
        self.click_choose_model()
        self.click_modification()
        self.click_catalog()
        self.click_bodywork()
        self.click_piston()
        self.click_search()
        self.click_select_product()



