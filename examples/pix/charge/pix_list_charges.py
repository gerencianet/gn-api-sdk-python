# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    "inicio": "2020-10-22T16:01:35Z",
    "fim": "2022-12-23T16:01:35Z"
}

response =  gn.pix_list_charges(params=params)
print(response)

