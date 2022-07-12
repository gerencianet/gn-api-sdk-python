# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

params = {
    'txid': ''
}

body = {
    'calendario': {
        'expiracao': 3600
    },
    'devedor': {
        'cpf': '',
        'nome': ''
    },
    'valor': {
        'original': '0.50'
    },
    'chave': '',
    'solicitacaoPagador': 'Cobrança dos serviços prestados.'
}

response =  gn.pix_create_charge(params=params,body=body)
print(response)
