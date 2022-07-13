# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    "inicio": "2021-01-14T16:01:35Z",
    "fim": "2022-12-15T16:01:35Z"
}

response =  gn.pix_received_list(params=params)
print(response)

