from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage): # наслідуємо клас від класу Base page
    URL = "https://github.com/login" # лінк зберігаємо в атрибуті класу

    def __init__(self):
        super().__init__() # виклик конструктора базового класу

    def go_to(self): # метод запускає браузер
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        # знаходимо поле в яке будемо вводити неправильне ім'я користувача
        login_element = self.driver.find_element(By.ID, "login_field")

        # знаходимо поле в яке будемо вводити неправильний пароль користувача
        pass_element = self.driver.find_element(By.ID, "password")

        # вводимо неправильне ім'я користувача
        login_element.send_keys(username)

        # вводимо неправильний пароль
        pass_element.send_keys(password)

        # знаходимо кнопку sign in
        btn_element = self.driver.find_element(By.NAME, "commit")

        # емулюємо клік
        btn_element.click()

    def check_title(self, expected_title):
        self.driver.title == expected_title

