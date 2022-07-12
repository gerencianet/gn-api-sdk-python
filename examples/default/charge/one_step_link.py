# encoding: utf-8

from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)


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

response =  gn.one_step_link(body=body)
print(response)
