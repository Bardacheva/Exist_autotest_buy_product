from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger
import allure

class Login_page(Base):

    url = 'https://exist.ru/'

    check_word = ''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    profile = "//div[@class='h']"
    user_name = "//input[@id='login']"
    password = "//input[@type='password']"
    login_button = "//input[@id='btnLogin']"
    main_word = "//span[contains(text(), 'Личный кабинет')]"


    # Getters

    def get_profile(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.profile)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        main_word = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word)))
        Login_page.check_word = main_word.text
        return Login_page.check_word

    # Actions

    def click_profile(self):
        self.get_profile().click()
        print("Click profile")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input login")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods
    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_profile()
            self.input_user_name("")
            self.input_password("")
            self.click_login_button()
            self.get_main_word()
            self.assert_word(Login_page.check_word, 'Личный кабинет') # проверяем, появилось ли 'Личный кабинет' на странице
            Logger.add_end_step(url=self.driver.current_url, method="authorization")