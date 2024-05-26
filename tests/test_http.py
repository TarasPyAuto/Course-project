import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen') #робимо get апит на цей сайт
    print(r.text)# r.test - для того шоб нам результат запиту текстом повернувся у консоль, без .test виведе просто <Response [200]>

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers

    assert body['name'] == 'Chris Wanstrath' # перевірка тіла
    assert r.status_code == 200 # перевірка статус коду
    assert headers['Server'] == 'GitHub.com' # перевірка заголовкa

@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')

    assert r.status_code == 404
