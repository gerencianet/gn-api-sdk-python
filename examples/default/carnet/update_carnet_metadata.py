# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    'id': 1
}

body = {
    'notification_url': 'http://yourdomain.com',
    'custom_id': 'my_new_id'
}

response =  gn.update_carnet_metadata(params=params, body=body)
print(response)
