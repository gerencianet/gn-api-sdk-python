# encoding: utf-8

from gerencianet import Gerencianet
from ..credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

response = gn.of_detail_settings()
print(response)