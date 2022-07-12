# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    'chave': ''
}

response =  gn.pix_get_webhook(params=params)
print(response)
