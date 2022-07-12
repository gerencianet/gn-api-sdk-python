# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    'id': 1
}

payment = {
    'payment': {
        'banking_billet': {
            'expire_at': '2022-12-12',
            'customer': {
                'name': "Gorbadoc Oldbuck",
                'email': "oldbuck@gerencianet.com.br",
                'cpf': "94271564656",
                'birth': "1977-01-15",
                'phone_number': "5144916523"
            }
        }
    }
}

response =  gn.pay_charge_billet(params=params, body=payment)
print(response)
