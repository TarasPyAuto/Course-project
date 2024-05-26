import pytest
from modules.api.clients.github import GitHub

@pytest.mark.api
def test_user_exist(github_api): # метод перевіряє чи існує користувач
    user = github_api.get_user('defunkt') # в змінну user повернули інформацію про користувача
    assert user['login'] == 'defunkt' # перевірили, що ім'я юзера - defunkt

@pytest.mark.api
def test_user_not_exist(github_api):  # метод перевіряє чи існує користувач, github_api фікстура в файлі conftest.py

    r = github_api.get_user('butenkosergii')  # в змінну user повернули інформацію про користувача
    print(r) # щоб подивитися в терміналі що нам вертається коли такого користувача не існує
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api): #тест на те що репозиторій існує
    r = github_api.search_repo('become-qa-auto') # шукаємо репозиторій з такою назвою
    print(r['total_count']) # перевіряю скільки зараз є репозиторіїв з такою назвою r- це словник, доступаюсь по ключу total_count
    print(r['items'][0])

    assert r['total_count'] == 57 # перевіряю що таких репозиторіїв всього 57
    assert 'become-qa-auto' in r['items'][0]['name'] # перевіряємо що перший знайдений репозиторій міститиме ім'я become-qa-auto

@pytest.mark.api
def test_repo_cannot_be_found(github_api): #тест на те що репозиторій НЕ існує
    r = github_api.search_repo('taras_yakushevych_repo') # шукаємо репозиторій з такою назвою
    assert r['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api): # задача методу перевірити, що існують репозиторії з довжиною в 1 символ
    r = github_api.search_repo('s')
    print(r['total_count'])
    assert r['total_count'] != 0
