import requests
from constants import Constants


class TestNewCourierApi:
     def test_new_courier_api(self, create_new_courier_and_del):
         payload = create_new_courier_and_del
         response = requests.post(Constants.URL + '/api/v1/courier', data=payload)
         r = response.json()
         assert response.status_code == 201
         assert r['ok']

