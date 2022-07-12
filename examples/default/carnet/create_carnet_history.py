# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
    'description': 'This carnet is about a service'
}

response =  gn.create_carnet_history(params=params, body=body)
print(response)
