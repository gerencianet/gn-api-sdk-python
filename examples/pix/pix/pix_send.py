# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)


params = {
    "idEnvio": 1
}

body = {
    'valor': '0.01',
    'pagador': {
        'chave': ''
    },
    'favorecido': {
        'chave': ''
    }
}

response =  gn.pix_send(params=params, body=body)
print(response)

