
import requests

from constants import Constants


class TestUserSameLogin:
    def test_user_same_login(self, generate_random_string, create_new_courier_and_del):
        payload = create_new_courier_and_del
        login = payload['login']
        payload_same_login = {'login': login, "password": generate_random_string, "firstName": generate_random_string}
        print(login)
        requests.post(Constants.URL + '/api/v1/courier', data=payload)
        response = requests.post(Constants.URL + '/api/v1/courier', data=payload_same_login)
        r = response.json()
        assert response.status_code == 409
        assert r['message'] == "Этот логин уже используется"
        #тест падает т.к. по документации другое сообщение