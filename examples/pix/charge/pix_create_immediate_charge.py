# encoding: utf-8

from gerencianet import Gerencianet
from ...credentials import credentials

gn = Gerencianet(credentials.CREDENTIALS)

body = {
    'calendario': {
        'expiracao': 3600
    },
    'devedor': {
        'cpf': '',
        'nome': ''
    },
    'valor': {
        'original': ''
    },
    'chave': '',
    'solicitacaoPagador': 'Cobrança dos serviços prestados.'
}

response =  gn.pix_create_immediate_charge(body=body)
print(response)
