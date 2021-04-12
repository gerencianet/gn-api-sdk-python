# encoding: utf-8

from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

body = {
    'items': [{
        'name': "Product 1",
        'value': 1000,
        'amount': 2
    }],
    'shippings': [{
        'name': "Default Shipping Cost",
        'value': 100
    }]
}

link = {
    'billet_discount': 0,
    'card_discount': 0,
    'message': '',
    'expire_at': '2017-12-12',
    'request_delivery_address': None,
    'payment_method': 'all'
}


charge = gn.create_charge(body=body)

params = {
    'id': charge['data']['charge_id']
}

response = gn.charge_link(params=params, body=link)
print(response)
