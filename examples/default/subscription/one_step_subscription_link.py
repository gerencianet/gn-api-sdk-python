# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    "id": 1
}

body = {
    'items': [{
        'name': "Product One",
        'value': 600,
        'amount': 1
    }],
    "settings": {
        'payment_method': 'all',
        'expire_at': '2022-12-15',
        'request_delivery_address': False
    }
}

response =  gn.one_step_subscription_link(params=params, body=body)
print(response)
