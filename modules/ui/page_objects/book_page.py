# not for test it's not completed
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class BookPage(BasePage): # наслідуємо клас від класу Base page
    URL = "https://bookclub.ua/catalog/books/thriller_horror_books/golli?search=%D0%B3%D0%BE%D0%BB%D0%BB%D1%96" # лінк зберігаємо в атрибуті класу

    def __init__(self):
        super().__init__() # виклик конструктора базового класу

    def go_to(self): # метод запускає браузер
        self.driver.get(BookPage.URL)

    def add_to_cart(self):

        cart_button = self.driver.find_element(By.CLASS_NAME, "cartimg.cart--main")

        cart_button.click()



    def go_to_cart(self):

        cart_icon = self.driver.find_element(By.CLASS_NAME, "cart-icon")

        cart_icon.click()

    def change_item_qnt_in_the_cart(self, qnt):

       input_field = self.driver.find_element(By.ID, "count61827")

       input_field.send_keys(qnt)

       click_block = self.driver.find_element(By.CLASS_NAME, "cartorderinp")

       click_block.click()


