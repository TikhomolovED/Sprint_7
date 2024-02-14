import requests

from constants import Constants


class TestLoginCourier:
    def test_login_courier(self, create_new_courier_and_del):
        payload = create_new_courier_and_del
        payload_login = payload
        payload_login.pop('firstName')
        requests.post(Constants.URL + '/api/v1/courier', data=payload)
        response = requests.post(Constants.URL+'/api/v1/courier/login', data=payload_login)

        assert response.status_code == 200
        assert 'id' in response.json()