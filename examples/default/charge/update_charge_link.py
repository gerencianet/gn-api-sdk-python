# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
    'billet_discount': 0,
    'card_discount': 0,
    'message': '',
    'expire_at': '2018-12-12',
    'request_delivery_address': False,
    'payment_method': 'all'
}

response = gn.update_charge_link(params=params, body=body)
print(response)
