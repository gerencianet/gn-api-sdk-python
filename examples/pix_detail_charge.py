from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    'txid': ''
}

response =  gn.pix_detail_charge(params=params)
print(response)
