

import requests

from constants import Constants


class TestGettingListOrders:
    def test_getting_list_orders_api(self):
        response = requests.get(Constants.URL + '/api/v1/orders')
        r = response.json()
        print(r)
        assert "orders" in r

