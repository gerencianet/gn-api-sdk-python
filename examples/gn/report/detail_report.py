# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    "id": "085y2253-bb04-48ba-b7d1-961538d0ed77"
}

response = gn.detail_report(params=params)
print(response)