# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)


params = {
    'id': 1
}

body = {
    'description': "This charge was not fully paid"
}

response =  gn.create_charge_history(params=params, body=body)
print(response)
