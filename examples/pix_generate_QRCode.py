from gerencianet import Gerencianet
from credentials import CREDENTIALS
import base64

gn = Gerencianet(CREDENTIALS)

params = {
    'id': 0
}

response =  gn.pix_generate_QRCode(params=params)
print(response)

#Generate QRCode Image
if('imagemQrcode' in response):
    with open("qrCodeImage.png", "wb") as fh:
        fh.write(base64.b64decode(response['imagemQrcode'].replace('data:image/png;base64,', '')))