import requests

from constants import Constants


class TestDoubleCourierApi:
    def test_double_courier_api(self, create_new_courier_and_del):
        payload = create_new_courier_and_del
        requests.post(Constants.URL + '/api/v1/courier', data=payload)
        response_double = requests.post(Constants.URL + '/api/v1/courier', data=payload)
        r_double = response_double.json()
        assert response_double.status_code == 409
        assert r_double['message'] == "Этот логин уже используется"
        #тест падает т.к. ответ задавался согласно документации