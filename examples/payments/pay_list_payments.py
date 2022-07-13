# encoding: utf-8

from gerencianet import Gerencianet
from ..credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    "dataInicio": "2020-10-22",
    "dataFim": "2022-06-23"
}

response = gn.pay_list_payments(params=params)
print(response)