### Resending the carnet

To resend the carnet, it must have a `active` status.

If the carnet contemplates this requirement, you just have to provide the carnet id and a email to resend it:

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
    'email': 'oldbuck@gerencianet.com.br'
}

response =  gn.resend_carnet(params=params, body=body)
print(response)

```

If everything goes well, the return will be:

```python
{
  "code": 200
}
```
