# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
    'expire_at': '2018-12-12'
}

response =  gn.update_billet(params=params, body=body)
print(response)
