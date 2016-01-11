### Resending billet

To resend the charge's billet, the charge must have a `waiting` status, and the payment method chosen must be `banking_billet`.

If the charge contemplates these requirements, you just have to provide the charge id and a email to resend the billet:

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

response =  gn.resend_billet(params=params, body=body)
print(response)

```

If everything goes well, the return will be:

```python
{
  "code": 200
}
```
