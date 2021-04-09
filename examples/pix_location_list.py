from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    "inicio": "2021-03-22T00:00:00.000Z",
    "fim": "2021-03-31T00:00:00.000Z"
}

response =  gn.pix_location_list(params=params)
print(response)

