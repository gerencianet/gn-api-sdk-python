# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    'e2eId': ''
}

response =  gn.pix_send_list(params=params)
print(response)

