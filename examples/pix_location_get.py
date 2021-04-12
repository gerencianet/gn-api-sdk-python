from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    'id': 0
}

response =  gn.pix_location_get(params=params)
print(response)

