# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    'id': 1,
    'parcel': 1
}

response = gn.cancel_parcel(params=params)
print(response)
