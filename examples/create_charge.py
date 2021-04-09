# encoding: utf-8

from gerencianet import Gerencianet
from credentials import CREDENTIALS


gn = Gerencianet(CREDENTIALS)

body = {
    'items': [{
        'name': "Product 1",
        'value': 1100,
        'amount': 2
    }],
    'shippings': [{
        'name': "Default Shipping Cost",
        'value': 100
    }]
}

response =  gn.create_charge(body=body)
print(response)
