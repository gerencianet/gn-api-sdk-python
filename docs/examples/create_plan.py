# encoding: utf-8

from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

body = {
    'name': "My first plan",
    'repeats': 24,
    'interval': 2
}

response =  gn.create_plan(body=body)
print(response)
