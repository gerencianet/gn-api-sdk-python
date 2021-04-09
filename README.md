# gn-api-sdk-python

> A python library for integration of your backend with the payment services
provided by [Gerencianet](http://gerencianet.com.br).

[![Build Status](https://travis-ci.org/gerencianet/gn-api-sdk-python.svg)](https://travis-ci.org/gerencianet/gn-api-sdk-python)
[![Coverage Status](https://coveralls.io/repos/gerencianet/gn-api-sdk-python/badge.svg?branch=master&service=github)](https://coveralls.io/github/gerencianet/gn-api-sdk-python?branch=master)
[![Code Climate](https://codeclimate.com/github/gerencianet/gn-api-sdk-python/badges/gpa.svg)](https://codeclimate.com/github/gerencianet/gn-api-sdk-python)

## Installation

Install with Pip:

```bash
$ pip install gerencianet
```
## Tested with
```
python 2.7, 3.3, 3.4, 3.5 and 3.9
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

You can run the examples inside `examples` with
`$ python examples/example.py`:

```bash
$ python examples/create_charge.py
```

Just remember to set the correct credentials inside `examples/credentials.py` before running.

## Tests

To run the tests, just run *pytest*:

```bash
$ py.test
```

## Additional documentation

The full documentation with all available endpoints is in https://dev.gerencianet.com.br/.

## Changelog

[CHANGELOG](CHANGELOG.md)

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/gerencianet/gn-api-sdk-python. This project is intended to be a safe, welcoming space for collaboration.

## License

The library is available as open source under the terms of the [MIT License](LICENSE).
