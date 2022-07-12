# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    'e2eId': ''
}

response =  gn.pix_detail(params=params)
print(response)

