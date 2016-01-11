## Updating carnets

### Changing the metadata

You can update the `custom_id` and the `notification_url` of a carnet at any time.

It's important to keep in mind that all the charges of the carnet will be updated. If you want to update only one charge, check [Updating charges](/docs/charge-update.md).

```python
# encoding: utf-8

from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    'id': 1
}

body = {
    'notification_url': 'http://yourdomain.com',
    'custom_id': 'my_new_id'
}

response =  gn.update_carnet_metadata(params=params, body=body)
print(response)

```

If everything goes well, the response will be:

```python
{
  "code": 200
}
```

### Updating the expiration date of a parcel

Only parcels with status `waiting` or `unpaid` can have expiration date set or updated:

```python
# encoding: utf-8

from gerencianet import Gerencianet
from credentials import CREDENTIALS

gn = Gerencianet(CREDENTIALS)

params = {
    'id': 1,
    'parcel': 1
}

body = {
    'expire_at': '2020-12-12'
}

response =  gn.update_parcel(params=params, body=body)
print(response)

```

If everything goes well, the response will be:

```python
{
  "code": 200
}
```
