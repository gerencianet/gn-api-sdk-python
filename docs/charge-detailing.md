## Detailing charges

It's very simple to get details from a charge. You just need the id:

```python
# encoding: utf-8

from gerencianet import Gerencianet

credentials = {
    'client_id': 'client_id',
    'client_secret': 'client_secret',
    'sandbox': True
}

gn = Gerencianet(credentials)

params = {
    'id': 1
}

response =  gn.detail_charge(params=params)
print(response)

```

As response, you will receive all the information about the charge (including if it belongs to a subscription or carnet):

```python
{
  "code": 200,
  "data": {
    "charge_id": 1300,
    "subscription_id": 12,
    "total": 2000,
    "status": "new",
    "custom_id": None,
    "created_at": "2015-05-14",
    "notification_url": "http://yourdomain.com",
    "items": [
      {
        "name": "Product 1",
        "value": 1000,
        "amount": 2
      }
    ],
    "history": [
      {
        "message": "Cobrança criada",
        "created_at": "2015-05-14 15:39:14"
      }
    ]
  }
}
```
