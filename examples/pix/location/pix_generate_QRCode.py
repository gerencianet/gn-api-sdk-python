# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials
import base64

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    'id': 1
}

response =  gn.pix_generate_QRCode(params=params)
print(response)

#Generate QRCode Image
if('imagemQrcode' in response):
    with open("qrCodeImage.png", "wb") as fh:
        fh.write(base64.b64decode(response['imagemQrcode'].replace('data:image/png;base64,', '')))