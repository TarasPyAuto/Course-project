import pytest

# тепер якщо не використовувати фікстури то треба вручну в кожному тесті додавати/видаляти користувача

@pytest.mark.check # групуємо ці тести у групу Check створюючи відмітку
def test_change_name(user):
    #user = User() # екземпляр класу
    #user.create()

    assert user.name == 'Taras'
    #user.remove()

@pytest.mark.check # групуємо ці тести у групу Check створюючи відмітку
def test_change_second_name(user):
    #user = User() # екземпляр класу
    #user.create()

    assert user.second_name == 'Yakushevych'
    #user.remove()
