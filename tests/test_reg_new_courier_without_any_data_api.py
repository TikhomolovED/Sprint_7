
import requests

from constants import Constants


class TestNewCourierWithoutAnyData:
    def test_courier_without_login(self, generate_random_string):

        payload = {'password': generate_random_string, 'firstname': generate_random_string}
        response = requests.post(Constants.URL + '/api/v1/courier', data=payload)
        r = response.json()
        assert response.status_code == 400
        assert r['message'] == "Недостаточно данных для создания учетной записи"

    def test_courier_without_password(self, generate_random_string):
        payload = {'login': generate_random_string, 'firstname': generate_random_string}
        response = requests.post(Constants.URL + '/api/v1/courier', data=payload)
        r = response.json()
        assert response.status_code == 400
        assert r['message'] == "Недостаточно данных для создания учетной записи"

    def test_courier_without_firstname(self, generate_random_string):
        payload = {'login': generate_random_string, 'password': generate_random_string}
        response = requests.post(Constants.URL + '/api/v1/courier', data=payload)
        r = response.json()
        assert response.status_code == 400
        assert r['message'] == "Недостаточно данных для создания учетной записи"
        #тест падает, т.к. запрос проходит без поля firstname