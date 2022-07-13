# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

body = {
    "dataMovimento": "2022-04-24",
    "tipoRegistros": {
        "pixRecebido": True,
        "pixDevolucaoEnviada": False,
        "tarifaPixRecebido": True,
        "pixEnviadoChave": True,
        "pixEnviadoDadosBancarios": False,
        "pixDevolucaoRecebida": True
    }
}

response = gn.create_report(body=body)
print(response)