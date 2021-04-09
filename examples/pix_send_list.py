from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    'e2eId': ''
}

response =  gn.pix_send_list(params=params)
print(response)

