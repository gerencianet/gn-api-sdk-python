# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
    'description': "This subscription was not fully paid"
}

response =  gn.create_subscription_history(params=params, body=body)
print(response)
