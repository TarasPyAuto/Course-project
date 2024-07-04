import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # для пошуку елементів на сторінці
import time

@pytest.mark.ui
def test_check_incorrect_username():
    # створення об'єкту для керування браузером
    #driver = webdriver.Chrome(service = Service(r"D:\\QA_Auto_course\\Git\\Final_project\\Course-project" + "chromedriver.exe"))

     # для версій 114 і ниєче
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    # відкриваємо сторінку логіну гітхаба(за допомогою метода get)
    driver.get("https://github.com/login")

    #знаходимо поле в яке будемо вводити неправильне ім'я користувача
    login_element = driver.find_element(By.ID, "login_field")

    # знаходимо поле в яке будемо вводити неправильний пароль користувача
    pass_element = driver.find_element(By.ID, "password")

    #вводимо неправильне ім'я користувача
    login_element.send_keys("taras.yakushevych@gmail.com")

    # вводимо неправильний пароль
    pass_element.send_keys("123245")

    # знаходимо кнопку sign in
    btn_element = driver.find_element(By.NAME, "commit")

    # емулюємо клік
    btn_element.click()

    #перевіряємо заголовок сторінки щоб переконатися, що ми знаходимося на тій сторінці що потрібно
    assert driver.title == "Sign in to GitHub · GitHub"

    time.sleep(3) #додаємо паузу потрібно видаляти після тестів

    # закриваємо браузер
    driver.close()