# encoding: utf-8

from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)


params = {
    'id': 1000
}

body = {
    'description': "This charge was not fully paid"
}

response =  gn.create_charge_history(params=params, body=body)
print(response)
