import pytest
# у всі тести передаємо нашу фікстуру

@pytest.mark.change
def test_remove_name(user): # тест перевіряє що я зможу видалити ім'я користувачу
    user.name = '' # видалили ім'я
    assert user.name == ''

@pytest.mark.check
def test_name(user): # тест перевіряє що ім'я Тарас
    assert user.name == 'Taras'

@pytest.mark.check
def test_second_name(user): # тест перевіряє що прізвище Якушевич
    assert user.second_name == 'Yakushevych'

# якщо запустимо ці тести зараз то 2 тест не пройде, бо не пройшов перший(перший тест видалив ім'я користувача)