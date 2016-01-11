## Creating subscriptions

If you ever have to recurrently charge your clients, you can create a different kind of charge, one that belongs to a subscription. This way, subsequent charges will be automatically created based on plan configuration and the charge value is charged in your customers' credit card, or the banking billet is generated and sent to the custumer, accoding to the plan’s configuration.

The plan configuration receive two params: `repeats` and `interval`:

The `repeats` parameter defines how many times the transaction will be repeated. If you don't provide it, the subscription will create charges indefinitely.

The `interval` parameter defines the interval, in months, that a charge has to be generated. The minimum value is 1, and the maximum is 24.

It's worth to mention that this mechanics is triggered only if the customer commits the subscription. In other words, it takes effect when the customer pays the first charge.

At last, it boils down to creating a plan and then the subscription. The plan can be reused for generating other subscriptions:

```python
# encoding: utf-8

from gerencianet import Gerencianet

credentials = {
    'client_id': 'client_id',
    'client_secret': 'client_secret',
    'sandbox': True
}

gn = Gerencianet(credentials)


body = {
    'name': "My first plan",
    'repeats': 24,
    'interval': 2
}

plan =  gn.create_plan(body=body)

params = {
    'id': plan['data']['plan_id']
}

body = {
    'items': [{
        'name': "Product 1",
        'value': 1000,
        'amount': 2
    }]
}

response =  gn.create_subscription(params=params, body=body)
print(response)

```

### Deleting a plan:
*(works just for plans that doesn't have a subscription associated):*

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

response =  gn.delete_plan(params=params)
print(response)
```

And the response
```python
{
  "code": 200
}
```


### Canceling subscriptions

You can cancel active subscriptions at any time:

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

response =  gn.cancel_subscription(params=params)
print(response)

```

Response:

```python
{
  "code": 200
}
```
