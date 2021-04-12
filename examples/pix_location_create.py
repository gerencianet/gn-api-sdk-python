from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

body = {
    'tipoCob': 'cob'
}

response =  gn.pix_location_create(body=body)
print(response)

