from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    'chave': ''
}

response =  gn.pix_delete_evp(params=params)
print(response)

