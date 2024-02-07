import requests

from constants import Constants


class TestLoginWithUncorrectData:
    def test_login_with_uncorrect_login(self, create_new_courier_and_del):
        payload = create_new_courier_and_del
        payload_login = payload.copy()
        payload_login.pop('firstName')
        payload_login['login'] = Constants.TEST_LOGIN
        requests.post(Constants.URL + '/api/v1/courier', data=payload)
        response = requests.post(Constants.URL+'/api/v1/courier/login', data=payload_login)
        r = response.json()

        assert response.status_code == 404
        assert r['message'] == "Учетная запись не найдена"

    def test_login_with_uncorrect_password(self, create_new_courier_and_del):
        payload = create_new_courier_and_del
        payload_login = payload.copy()
        payload_login.pop('firstName')
        payload_login['password'] = Constants.TEST_PASSWORD
        requests.post(Constants.URL + '/api/v1/courier', data=payload)
        response = requests.post(Constants.URL+'/api/v1/courier/login', data=payload_login)
        r = response.json()

        assert response.status_code == 404
        assert r['message'] == "Учетная запись не найдена"