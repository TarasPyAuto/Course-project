# not for test it's not completed
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class MainPage(BasePage): # наслідуємо клас від класу Base page
    URL = "https://bookclub.ua/" # лінк зберігаємо в атрибуті класу

    def __init__(self):
        super().__init__() # виклик конструктора базового класу

    def go_to(self): # метод запускає браузер
        self.driver.get(MainPage.URL)

    def search_book_with_a_valid_data(self, query):
        search_field = self.driver.find_element(By.CLASS_NAME, "bsearch.mobile_hide")

        search_field.click()

        search_input = self.driver.find_element(By.CLASS_NAME, "multi-input")

        search_input.send_keys(query)

        print(type(search_input))

        search_results = self.driver.find_element(By.CLASS_NAME, "multi-results.multi-content")
        print(type(search_results))

