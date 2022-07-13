# encoding: utf-8

from gerencianet import Gerencianet
from ..credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    "idPagamento": 1
}

response = gn.pay_detail_payment(params=params)
print(response)