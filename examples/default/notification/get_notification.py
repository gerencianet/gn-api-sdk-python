# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    'token': "252948279264ee47e117cb099ef81"
}

response =  gn.get_notification(params=params)
print(response)
