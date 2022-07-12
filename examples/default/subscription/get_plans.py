# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    'name': "My Plan",
    'limit': 1,
    'offset': 0
}

response =  gn.get_plans(params=params)
print(response)
