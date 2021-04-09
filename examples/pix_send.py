from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

body = {
    'valor': '',
    'pagador': {
        'chave': ''
    },
    'favorecido': {
        'chave': ''
    }
}

response =  gn.pix_send(body=body)
print(response)

