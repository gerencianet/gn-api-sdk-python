from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    "inicio": "2020-10-22T16:01:35Z",
    "fim": "2021-04-23T16:01:35Z"
}

response =  gn.pix_list_charges(params=params)
print(response)

