# encoding: utf-8

from gerencianet import Gerencianet
from ..credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    "codBarras": 1
}

response = gn.pay_detail_bar_code(params=params)
print(response)