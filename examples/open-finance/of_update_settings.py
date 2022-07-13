# encoding: utf-8

from gerencianet import Gerencianet
from ..credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

body = {
  "redirectURL": "https://gerencianet.com.br",
  "webhookURL": "https://gerencianetwh.tk/webhook"
}

response = gn.of_update_settings(body=body)
print(response)