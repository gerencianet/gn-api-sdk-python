# encoding: utf-8

from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    'id': 0
}

body = {
    'billet_discount': 0,
    'card_discount': 0,
    'message': '',
    'expire_at': '2018-12-12',
    'request_delivery_address': false,
    'payment_method': 'all'
}

response = gn.update_charge_link(params=params, body=body)
print(response)
