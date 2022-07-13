# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
    'name': 'My new plan'
}

response =  gn.update_plan(params=params, body=body)
print(response)
