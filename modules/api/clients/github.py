import requests

class GitHub:

    def get_user(self, username): # повертає body тобто дані про юзера
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return  body

    def search_repo(self, name): # метод для пошуку репозиторію
        r = requests.get('https://api.github.com/search/repositories', params = {"q" : name}) # передаємо параметр з ім'ям q, значення якого, це ім'я репозиторія який ми будемо шукати
        body = r.json()
        return body
