from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    'e2eId': '',
    'id': 0
}

response =  gn.pix_devolution_get(params=params)
print(response)

