# gn-api-sdk-python

> A python library for integration of your backend with the payment services
provided by [Gerencianet](http://gerencianet.com.br).

[![Build Status](https://travis-ci.org/dannielhugo/gn-api-sdk-python.svg)](https://travis-ci.org/dannielhugo/gn-api-sdk-python)
[![Coverage Status](https://coveralls.io/repos/dannielhugo/gn-api-sdk-python/badge.svg?branch=master&service=github)](https://coveralls.io/github/dannielhugo/gn-api-sdk-python?branch=master)
[![Code Climate](https://codeclimate.com/github/dannielhugo/gn-api-sdk-python/badges/gpa.svg)](https://codeclimate.com/github/dannielhugo/gn-api-sdk-python)


:warning: **THIS LIBRARY IS NOT PRODUTION VERSION YET. IT WILL BE RELEASED SOME TIME IN FUTURE IN OFFICIAL GERENCIANT'S GITHUB PAGE**

:warning: **Gerencianet API is under BETA version, meaning that it's not available for all users right now. If you're interested, you can always send an email to
desenvolvedores@gerencianet.com.br and we'll enable it for your account**

## Installation

Add this line to your application's Gemfile:

```bash
$ pip install gerencianet
```

## Basic usage

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
    'items': [{
        'name': "Product 1",
        'value': 1000,
        'amount': 2
    }],
    'shippings': [{
        'name': "Default Shipping Cost",
        'value': 100
    }]
}

print gn.create_charge(body=body)

```

## Examples

You can run the examples inside `docs/examples` with
`$ python docs/examples/example.py`:

```bash
$ python docs/examples/create_charge.py
```

Just remember to set the correct credentials inside `docs/examples/credentials.py` before running.

## Tests

To run the tests, just run *pytest*:

```bash
$ py.test
```

## Additional documentation

### Charges

- [Creating charges](/docs/charges.md)
- [Paying a charge](/docs/charge-payment.md)
- [Detailing charges](/docs/charge-detailing.md)
- [Updating informations](/docs/charge-update.md)
- [Resending billet](/docs/charge-resend-billet.md)
- [Adding information to charge's history](/docs/charge-create-history.md)

### Carnets

- [Creating carnets](/docs/carnets.md)
- [Detailing carnets](/docs/carnet-detailing.md)
- [Updating informations](/docs/carnet-update.md)
- [Resending the carnet](/docs/carnet-resend.md)
- [Resending carnet parcel](/docs/carnet-resend-parcel.md)
- [Adding information to carnet's history](/docs/carnet-create-history.md)

### Subscriptions

- [Creating subscriptions](/docs/subscriptions.md)
- [Paying a subscription](/docs/subscription-payment.md)
- [Detailing subscriptions](/docs/subscription-detailing.md)
- [Updating informations](/docs/subscription-update.md)

### Marketplace

- [Creating a marketplace](/docs/charge-with-marketplace.md)

### Notifications

- [Getting notifications](/docs/notifications.md)

### Payments

- [Getting installments](/docs/installments.md)

### All in one

- [Usage](/docs/all-in-one.md)

## Changelog

[CHANGELOG](CHANGELOG.md)

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/gerencianet/gn-api-sdk-python. This project is intended to be a safe, welcoming space for collaboration.

## License

The library is available as open source under the terms of the [MIT License](LICENSE).
