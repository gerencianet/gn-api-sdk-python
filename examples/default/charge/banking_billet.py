# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

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

payment = {
    'payment': {
        'banking_billet': {
            'expire_at': '2016-12-12',
            'customer': {
                'name': "Gorbadoc Oldbuck",
                'email': "oldbuck@gerencianet.com.br",
                'cpf': "04267484171",
                'birth': "1977-01-15",
                'phone_number': "5144916523"
            }
        }
    }
}


charge = gn.create_charge(body=body)

params = {
    'id': charge['data']['charge_id']
}


response = gn.pay_charge(params=params, body=payment)
print(response)
