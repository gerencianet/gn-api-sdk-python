## Detailing subscriptions

Works just like the charge detailing, but here you pass the subscription id:

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
    'id': 12
}

response =  gn.detail_subscription(params=params)
print(response)

```

Response:

```python
{
  "code": 200,
  "data": {
    "subscription_id": 12,
    "value": 2000,
    "status": "new",
    "payment_method": None,
    "next_execution": None,
    "next_expire_at": None,
    "interval": 1,
    "repeats": 2,
    "processed_amount": 0,
    "created_at": "2015-05-14 15:39:14",
    "history": [
      {
        "charge_id": 233,
        "status": "new",
        "created_at": "2015-05-14 15:39:14"
      }
    ]
  }
}
```

Note that if you [detail a charge](/docs/charge-detailing.md) that belongs to a subscription, the response will have a `subscription` block with data about it, including the `subscription_id`. If you need the subscription information, you can do this:

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
    'id': 233
}

charge = gn.detail_charge(params=params)

params = {
    'id': charge['data']['subscription_id']
}

response = gn.detail_subscription(params=params)
print(response)
```
