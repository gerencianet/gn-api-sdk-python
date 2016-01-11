## Adding information to carnet's history

It is possible to add information to the history of a carnet. These informations will be listed when [detailing a carnet](https://github.com/gerencianet/gn-api-sdk-python/tree/master/docs/carnet-detailing.md).

The process to add information to history is shown below:


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
    'description': 'This carnet is about a service'
}

response = gn.create_carnet_history(params=params, body=body)

print(response)
```

If everything goes well, the return will be:

```python
{
  "code": 200
}
```
