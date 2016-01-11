## Adding information to charge's history

It is possible to add information to the history of a charge. These informations will be listed when [detailing a charge](/docs/charge-detailing.md).

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
    'id': 1000
}

body = {
    'description': "This charge was not fully paid"
}

response =  gn.create_charge_history(params=params, body=body)
print(response)

```

If everything goes well, the return will be:

```python
{
  "code": 200
}
```
