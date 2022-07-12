# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

body = {
    'tipoCob': 'cob'
}

response =  gn.pix_location_create(body=body)
print(response)

