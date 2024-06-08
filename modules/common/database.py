import sqlite3 # модуль для взаємодії з бд


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(r'D:\\QA_Auto_course\\Git\\Final_project\\Course-project' + r'\\become_qa_auto.db') #  connection - сутність яка потрібна модулюдля взаємодії з бд
        self.cursor = self.connection.cursor() # сутність, яка може виконувати наші команди в бд

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query) # виконуємо запит до бд щоб отримати вкрсію бд
        record = self.cursor.fetchall() # отримання результатів запиту
        print(f'Connected successfully. SQLite Database version is: {record}')

    def get_all_users(self):
        query = 'SELECT name, address, city FROM customers'
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record # повертаємо результат виводу

    def get_user_address_by_name(self, name):
        query = f"SELECT  address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record # повертаємо результат виводу

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE  products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit() # підтверджуємло зміни в бд для того, щоб випадково не змінити те що не хотіли змінити

    def select_product_qnt_by_id(self, product_id): # метод для перевірки оновлення продукту по ID
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})" # INSERT OR REPLACE вставити або хамінити рядок якщо такий вже є
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM  products  WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = 'SELECT orders.id, customers.name, products.name, products.description, orders.order_date  FROM orders JOIN customers ON orders.customer_id = customers.id JOIN products ON orders.product_id = products.id'
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
