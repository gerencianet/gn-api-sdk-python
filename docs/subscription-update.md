## Updating subscriptions

### Changing the metadata

You can update the `custom_id` or the `notification_url` of a subscription.

It is important to keep in mind that all the subscription charges will be updated. If you want to update only one, check [Updating charges](/docs/charge-update).

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

response =  gn.update_subscription_metadata(params=params, body=body)
print(response)

```

If everything goes well, the return will be:

```python
{
  "code": 200
}
```
