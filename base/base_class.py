from datetime import datetime


class Base():
# Основные методы для всех классов

    def __init__(self, driver):
        self.driver = driver


    # Method get current url

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    # Method assert word

    def assert_word(self, word, result):
        assert word == result
        print("Successful verification of the value")


    # Method Screenshot

    def get_screenshot(self):
        now_date = datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot(f"C:\\Users\\Пользователь\\PycharmProjects\\Main_Project_sel\\screen\\{name_screenshot}")


    # Method assert URL

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")