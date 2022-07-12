# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    'id': 1,
    'parcel': 1
}

body = {
    'email': 'oldbuck@gerencianet.com.br'
}

response =  gn.resend_parcel(params=params, body=body)
print(response)
