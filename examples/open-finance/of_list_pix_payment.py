# encoding: utf-8

from gerencianet import Gerencianet
from ..credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    "inicio": "2020-10-22",
    "fim": "2022-12-23"
}

response = gn.of_list_pix_payment(params=params)
print(response)