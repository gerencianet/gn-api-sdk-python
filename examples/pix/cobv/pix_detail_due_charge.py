# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    "txid": ""
}

response = gn.pix_detail_due_charge(params=params)
print(response)