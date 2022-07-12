# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

body = {
    'name': "My first plan",
    'repeats': 24,
    'interval': 2
}

response =  gn.create_plan(body=body)
print(response)
