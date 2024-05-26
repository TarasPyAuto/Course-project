# цей файл спеціально призначений для зберігання всіх фікстур, а в самиї файлах з тестами зберігаються лише тести
#  і якщо одна фікстура використовується в різних файлах, то нам її треба змінити лише в цьому файлі

import pytest
from modules.api.clients.github import GitHub

class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Taras'
        self.second_name = 'Yakushevych'

    def remove(self):
        self.name = ''
        self.second_name = ''

@pytest.fixture
def user():
    user = User()
    user.create()



# все, що написано до слова yield відбувається до перевірки, тобто в даному випадку ми до перевірки створюємо екземпляр класу та викликаємо метод класу user.create
    yield user # тут повертаємо об'єкт user в тести

    user.remove() # а після перевірки видаляємо екземпляр і тупер в методах це можна закоментувати

@pytest.fixture
def github_api():
    api = GitHub()
    yield api