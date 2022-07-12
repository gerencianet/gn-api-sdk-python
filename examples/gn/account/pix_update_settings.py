# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

body = {
    'pix': {
        'receberSemChave': True,
        'chaves': {
            'insira-aqui-sua-chave': {
                'recebimento': {
                    'txidObrigatorio': False,
                    'qrCodeEstatico': {
                        'recusarTodos': False
                    }
                }
            }
        }
    }
}
response =  gn.pix_update_settings(body=body)
print(response)

