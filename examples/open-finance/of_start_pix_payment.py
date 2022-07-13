# encoding: utf-8

from gerencianet import Gerencianet
from ..credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

headers = {
    'x-idempotency-key': "et sedaute sint officiapariatur amet tute sum"
}

body = {
  "pagador": {
    "idParticipante": "75db457a-612d-4d62-b557-ba9d32b05216",
    "cpf": "12345678909",
  },
  "favorecido": {
    "contaBanco": {
      "codigoBanco": "364",
      "agencia": "0001",
      "documento": "01234567890",
      "nome": "Gerencianet Pagamentos",
      "conta": "200045",
      "tipoConta": "CACC"
    }
  },
  "valor": "0.01",
  "infoPagador": "Compra dia xx"
}

response = gn.of_start_pix_payment( body=body, headers=headers)
print(response)