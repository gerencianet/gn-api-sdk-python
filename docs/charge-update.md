## Updating charges

### Changing the metadata

You can update the `custom_id` or the `notification_url` of a charge:

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

body = {
    'notification_url': 'http://yourdomain.com',
    'custom_id': 'my_new_id'
}

response =  gn.update_charge_metadata(params=params, body=body)
print(response)

```

If everything goes well, the return will be:

```python
{
  "code": 200
}
```

### Updating the expiration date of a billet

Only charges with status `waiting` or `unpaid` and with payment method `banking_billet` can have the `expire_at` changed:

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

body = {
    'expire_at': '2018-12-12'
}

response =  gn.update_billet(params=params, body=body)
print(response)
```

If everything goes well, the return will be:

```python
{
  "code": 200
}
```
