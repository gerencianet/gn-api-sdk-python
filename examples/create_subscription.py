# encoding: utf-8

from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    'id': 1
}

body = {
    'items': [{
        'name': "Product 1",
        'value': 1000,
        'amount': 2
    }]
}

response =  gn.create_subscription(params=params, body=body)
print(response)
