## Create charge and payment

The most common case scenarios consist of the two steps mentioned in the title. The other examples show each part separately. Here goes the most used endpoints grouped in one example.

Create the inputs for the three endpoints:

```python
charge = {
    'items': [{
        'name': "Product 1",
        'value': 1000,
        'amount': 2
    }],
    'shippings': [{
        'name': "Default Shipping Cost",
        'value': 100
    }]
}

payment = {
    'payment': {
        'credit_card': {
            'installments': 1,
            'payment_token': "", #see credit card flow to see how to get this
            'billing_address': {
                'street': "Av. JK",
                'number': 909,
                'neighborhood': "Bauxita",
                'zipcode': "35400000",
                'city': "Ouro Preto",
                'state': "MG"
            },
            'customer': {
                'name': "Gorbadoc Oldbuck",
                'email': "oldbuck@gerencianet.com.br",
                'cpf': "04267484171",
                'birth': "1977-01-15",
                'phone_number': "5144916523"
            }
        }
    }
}
```

Call the endpoints:

```python
# encoding: utf-8

from gerencianet import Gerencianet

credentials = {
    'client_id': 'client_id',
    'client_secret': 'client_secret',
    'sandbox': True
}

gn = Gerencianet(credentials)

charge = gn.create_charge(body=body)

params = {
    'id': charge['data']['charge_id']
}


payment = gn.pay_charge(params=params, body=payment)

print(charge, payment)
```

Response:

```python
{
  "code": 200,
  "data": {
     "charge_id": 260,
     "total": 2250,
     "status": 'new',
     "custom_id": None,
     "created_at": "2015-05-18"
   }
} #charge created

{
  "code": 200,
  "data": {
     "charge_id": 260,
     "total": 2400,
     "payment": "credit_card",
     "installments": 1,
     "installment_value": 2400
  }
} #payment created
```
