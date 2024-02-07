import requests

from constants import Constants


class TestLoginWithoutAnyData:
    def test_login_without_login(self, create_new_courier_and_del):
        payload = create_new_courier_and_del
        payload_login = payload.copy()
        payload_login.pop('firstName')
        payload_login.pop('login')
        requests.post(Constants.URL + '/api/v1/courier', data=payload)
        response = requests.post(Constants.URL+'/api/v1/courier/login', data=payload_login)
        r = response.json()
        assert response.status_code == 400
        assert r['message'] == "Недостаточно данных для входа"


    def test_login_without_password(self, create_new_courier_and_del):
        payload = create_new_courier_and_del
        payload_login = payload.copy()
        payload_login.pop('firstName')
        payload_login.pop('password')
        requests.post(Constants.URL + '/api/v1/courier', data=payload)
        response = requests.post(Constants.URL+'/api/v1/courier/login', data=payload_login)
        r = response.json()
        assert response.status_code == 400
        assert r['message'] == "Недостаточно данных для входа"
        #тест падает, т.к. ручка уходит в Service unavailable

