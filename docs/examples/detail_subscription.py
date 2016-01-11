# encoding: utf-8

from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    'id': 1
}

response =  gn.detail_subscription(params=params)
print(response)
