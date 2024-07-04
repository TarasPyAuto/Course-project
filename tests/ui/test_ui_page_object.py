from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.main_page import MainPage
from modules.ui.page_objects.book_page import BookPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    sign_in_page = SignInPage()  #створення об'єкту сторінки

    sign_in_page.go_to() # відкриваємо сторінку

    sign_in_page.try_login("page_object@gmail.com", "wrong password") # спроба входу

    assert sign_in_page.check_title("Sign in to GitHub · GitHub") # перевіряємо заголовок

    sign_in_page.close()  # закриваємо браузер

@pytest.mark.search # not for test it's not completed
def test_search_with_a_valid_data():
    main_page = MainPage()

    main_page.go_to()

    main_page.search_book_with_a_valid_data("голлі")


    main_page.close()

@pytest.mark.cart # not for test it's not completed
def test_add_book_to_the_cart():
    book_page = BookPage()

    book_page.go_to()

    book_page.add_to_cart()

    book_page.go_to_cart()

    book_page.close



@pytest.mark.cart
def test_change_qnt_with_a_valid_data():
    book_page = BookPage()

    test_add_book_to_the_cart()

    book_page.change_item_qnt_in_the_cart(25)

