# encoding: utf-8

from gerencianet import Gerencianet
from ..credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    "codBarras": 1
}

body = {
    "valor": 9300,
    "dataPagamento": "2022-06-17",
    "descricao": "Pagamento de boleto, teste API Pagamentos"
}

response = gn.pay_request_bar_code(params=params, body=body)
print(response)