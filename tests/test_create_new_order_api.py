import json

import pytest
import requests

from constants import Constants


class TestCreateNewOrder:
    @pytest.mark.parametrize('color', [["GREY"], ["BLACK"], ["BLACK", "GREY"], []])
    def test_create_new_order_api(self, color):
        payload = json.dumps({
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": color
        })

        response = requests.post(Constants.URL + '/api/v1/orders', data=payload)
        r = response.json()
        assert 'track' in r
