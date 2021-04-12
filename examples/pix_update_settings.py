from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

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

