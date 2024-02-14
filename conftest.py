import requests
import random
import string
import pytest

from constants import Constants


@pytest.fixture
def generate_random_string():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(7))
    return random_string


@pytest.fixture
def create_new_courier_and_del(generate_random_string):
    password = generate_random_string
    login = generate_random_string
    user = {'login': login, "password": password, "firstName": "saske"}
    user_login = {'login': login, "password": password}
    yield user
    response = requests.post(Constants.URL + '/api/v1/courier/login', data=user_login)
    id_courier = response.json()['id']
    requests.delete(Constants.URL + f'/api/v1/courier/{id_courier}')

