from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    "inicio": "2021-01-14T16:01:35Z",
    "fim": "2021-04-15T16:01:35Z"
}

response =  gn.pix_received_list(params=params)
print(response)

