# encoding: utf-8

from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    'brand': 'visa',
    'total': 5000
}

response =  gn.get_installments(params=params)
print(response)
