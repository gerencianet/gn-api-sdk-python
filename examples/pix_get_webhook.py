from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    'chave': ''
}

response =  gn.pix_get_webhook(params=params)
print(response)
