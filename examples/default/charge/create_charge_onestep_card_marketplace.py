# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

body = {
    'items': [{
        'name': "Product 1",
        'value': 1000,
        'amount': 2,
        'marketplace': {
            'mode': 1,
            'repasses': [{
                'payee_code': "Insira_aqui_o_indentificador_da_conta_destino",
                'percentage': 2500
            }]
          }
    }],
    'shippings': [{
        'name': "Default Shipping Cost",
        'value': 100
    }],
    'payment': {
        'credit_card': {
            'installments': 1,
            'payment_token': "InsiraAquiUmPayeementeCode",
            'billing_address': {
                'street': "Av. JK",
                'number': 909,
                'neighborhood': "Bauxita",
                'zipcode': "35400000",
                'city': "Ouro Preto",
                'state': "MG"
            },
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
response = gn.create_charge_onestep(params=None, body=body)
print(response)