from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    'e2eId': '',
    'id': 0
}

body = {
    'valor': ''
}

response =  gn.pix_devolution(params=params,body=body)
print(response)

