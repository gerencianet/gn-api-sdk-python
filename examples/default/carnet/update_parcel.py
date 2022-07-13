# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    'id': 1,
    'parcel': 1
}

body = {
    'expire_at': '2020-12-12'
}

response =  gn.update_parcel(params=params, body=body)
print(response)
