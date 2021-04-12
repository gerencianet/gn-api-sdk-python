from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    'txid': ''
}

body = {
    'calendario': {
        'expiracao': 600
    },
    'devedor': {
        'nome': '',
        'cpf': ''
    },
    'valor': {
        'original': ''
    },
    'chave': '',
    'solicitacaoPagador': None,
    'infoAdicionais': [
        {
            'nome': 'Nome 01',
            'valor': 'valor 01'
        }
    ]
}

response =  gn.pix_update_charge(params=params,body=body)
print(response)

