# encoding: utf-8

from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    'id': 1,
    'parcel': 1
}

response = gn.settle_carnet_parcel(params=params)
print(response)
