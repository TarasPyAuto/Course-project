import pytest
from modules.common.database import Database

@pytest.mark.database
def test_database_connection(database_test):
    database_test.test_connection()

@pytest.mark.database
def test_check_all_users(database_test):
    users = database_test.get_all_users()
    print(users)

@pytest.mark.database
def test_check_user_sergii(database_test):
    user = database_test.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1' # user[0][0] - перший індекс це індекс рядка в таблиці
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update(database_test):
    database_test.update_product_qnt_by_id(1,25) # виклик методу з update запитом
    water_qnt = database_test.select_product_qnt_by_id(1) # показали оновлення

    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert(database_test):
    database_test.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = database_test.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete(database_test):
    database_test.insert_product(99, 'тестові', 'дані', 999) # при тестуванні видалення даних завжди створюємо тестові дані, щоб випадково не видалити те, що потрібно
    database_test.delete_product_by_id(99)
    qnt = database_test.select_product_qnt_by_id(99) # вибираємо товар з ID яке ми щойно видалили
    assert len(qnt) == 0 # перевіряємо що довжина масиву знайдених результатів - 0

@pytest.mark.database
def test_detailed_orders(database_test):
    orders = database_test.get_detailed_orders()
    print("Замовлення", orders)
    assert len(orders) == 1 # перевірка кількості результатів

    # перевірка даних і структури
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'

