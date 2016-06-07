### Canceling carnet parcel

You can cancel carnet parcel. To this, the charge status must be `new`, `waiting` or `unpaid`.

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
    'id': 1, 
    'parcel': 1
}

response =  gn.cancel_parcel(params=params, body=body)
print(response)

```

If everything goes well, the return will be:

```python
{
  "code": 200
}
```
