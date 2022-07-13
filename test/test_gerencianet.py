# encoding: utf-8

import pytest
import responses
import requests
import os

from gerencianet import Gerencianet
from gerencianet import Constants

from gerencianet import MissingParametersError
from gerencianet import UnauthorizedError


class TestGerencianet():
    auth_success = {u'access_token': u'token', u'token_type': u'Bearer',
                    u'expires_in': 600, u'refresh_token': u'refresh'}

    charge = {u'code': 200, u'data': {u'status': u'new', u'created_at': u'2016-01-08 11:05:21',
                                      u'custom_id': None, u'total': 3000, u'charge_id': 1724}}


    def test_remove_placeholders(self):
        endpoints = Gerencianet({})
        fixed_route = endpoints.remove_placeholders(
            Constants.APIS['DEFAULT']['ENDPOINTS']['detail_charge']['route'], {'id': 1})
        assert fixed_route == '/charge/1'

        fixed_route = endpoints.remove_placeholders(
            Constants.APIS['DEFAULT']['ENDPOINTS']['create_charge']['route'], {})
        assert fixed_route == '/charge'

        fixed_route = endpoints.remove_placeholders(
            Constants.APIS['DEFAULT']['ENDPOINTS']['update_parcel']['route'], {'id': 1, 'parcel': 2})
        assert fixed_route == '/carnet/1/parcel/2'

        with pytest.raises(MissingParametersError) as raised:
            fixed_route = endpoints.remove_placeholders(
                Constants.APIS['DEFAULT']['ENDPOINTS']['update_parcel']['route'], {'id': 1})
        assert 'ExceptionInfo MissingParametersError(\'parcel\')' in str(raised)

    def test_query_string(self):
        endpoints = Gerencianet({})

        qs = endpoints.query_string(
            {'age': 78, 'name': 'Gorbadoc', 'lastname': 'Oldbuck'})
        assert all(x in qs for x in ['lastname=Oldbuck', 'age=78', 'name=Gorbadoc', '&'])
