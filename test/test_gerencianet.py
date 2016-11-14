# encoding: utf-8

import pytest
import responses
import requests

from gerencianet import Gerencianet
from gerencianet import Constants

from gerencianet import MissingParametersError
from gerencianet import UnauthorizedError


class TestGerencianet():
    auth_success = {u'access_token': u'token', u'token_type': u'Bearer',
                    u'expires_in': 600, u'refresh_token': u'refresh'}

    charge = {u'code': 200, u'data': {u'status': u'new', u'created_at': u'2016-01-08 11:05:21',
                                      u'custom_id': None, u'total': 3000, u'charge_id': 1724}}

    def test_base_url(self):
        endpoints = Gerencianet({})
        assert endpoints.base_url == Constants.URL['sandbox']

        endpoints = Gerencianet({'sandbox': True})
        assert endpoints.base_url == Constants.URL['sandbox']

        endpoints = Gerencianet({'sandbox': False})
        assert endpoints.base_url == Constants.URL['production']

    def test_remove_placeholders(self):
        endpoints = Gerencianet({})
        fixed_route = endpoints.remove_placeholders(
            Constants.ENDPOINTS['detail_charge']['route'], {'id': 1})
        assert fixed_route == '/charge/1'

        fixed_route = endpoints.remove_placeholders(
            Constants.ENDPOINTS['create_charge']['route'], {})
        assert fixed_route == '/charge'

        fixed_route = endpoints.remove_placeholders(
            Constants.ENDPOINTS['update_parcel']['route'], {'id': 1, 'parcel': 2})
        assert fixed_route == '/carnet/1/parcel/2'

        with pytest.raises(MissingParametersError) as raised:
            fixed_route = endpoints.remove_placeholders(
                Constants.ENDPOINTS['update_parcel']['route'], {'id': 1})

        assert 'Missing required parameter parcel' in str(raised)
        # out = capsys.readouterr()

    def test_query_string(self):
        endpoints = Gerencianet({})

        qs = endpoints.query_string(
            {'age': 78, 'name': 'Gorbadoc', 'lastname': 'Oldbuck'})
        assert all(x in qs for x in ['lastname=Oldbuck', 'age=78', 'name=Gorbadoc', '&'])

    def test_build_url(self):
        endpoints = Gerencianet({})

        #test parameter completion
        url = endpoints.build_url(
            Constants.ENDPOINTS['detail_charge']['route'], {'id': 1})
        assert url == Constants.URL['sandbox'] + '/charge/1'

        #test multiple parameter completion
        url = endpoints.build_url(Constants.ENDPOINTS['update_parcel'][
                                  'route'], {'id': 1, 'parcel': 2})
        assert url == Constants.URL['sandbox'] + '/carnet/1/parcel/2'

        #test querystring
        url = endpoints.build_url(Constants.ENDPOINTS['get_installments'][
                                  'route'], {'brand': 'visa', 'total': 1000})
        assert all(x in url for x in  [Constants.URL['sandbox'] + '/installments' , 'brand=visa', 'total=1000'])

        #test querystring with url parameters
        url = endpoints.build_url(Constants.ENDPOINTS['detail_charge']['route'], {
                                  'id': 1, 'status': 'new', 'value': 1000})
        assert all(x in url for x in [Constants.URL['sandbox'] + '/charge/1', 'status=new', 'value=1000'])
        # out = capsys.readouterr()

    @responses.activate
    def test_authenticate_success(self):
        responses.add(responses.POST, Constants.URL['sandbox'] + '/authorize',
                      content_type='application/json', status=200,
                      json=TestGerencianet.auth_success)

        endpoints = Gerencianet({'client_id': 'cid', 'client_secret': 'csec'})
        endpoints.authenticate()

        assert endpoints.token == TestGerencianet.auth_success
        # out = capsys.readouterr()

    @responses.activate
    def test_authenticate_failure(self):
        responses.add(responses.POST, Constants.URL['sandbox'] + '/authorize',
                      content_type='application/json', status=401)

        endpoints = Gerencianet({'client_id': 'cid', 'client_secret': 'csec'})

        with pytest.raises(UnauthorizedError) as raised:
            endpoints.authenticate()

        assert '401' in str(raised)

    @responses.activate
    def test_api_request_call_success(self):
        responses.add(responses.POST, Constants.URL['sandbox'] + '/authorize',
                      content_type='application/json', status=200,
                      json=TestGerencianet.auth_success)

        responses.add(responses.POST, Constants.URL['sandbox'] + '/charge',
                      content_type='application/json', status=200,
                      json=TestGerencianet.charge)

        items = [
            {'name': 'item 1', 'value': 1000},
            {'name': 'item 2', 'value': 2000}
        ]

        endpoints = Gerencianet({'client_id': 'cid', 'client_secret': 'csec'})
        response = endpoints.create_charge(body={'items': items})

        assert response == TestGerencianet.charge

    @responses.activate
    def test_api_request_call_unauthorized(self):
        responses.add(responses.POST, Constants.URL['sandbox'] + '/charge',
                      content_type='application/json', status=401,
                      json=TestGerencianet.charge)

        responses.add(responses.POST, Constants.URL['sandbox'] + '/authorize',
                      content_type='application/json', status=200,
                      json=TestGerencianet.auth_success)

        responses.add(responses.POST, Constants.URL['sandbox'] + '/charge',
                      content_type='application/json', status=200,
                      json=TestGerencianet.charge)

        items = [
            {'name': 'item 1', 'value': 1000},
            {'name': 'item 2', 'value': 2000}
        ]

        endpoints = Gerencianet({'client_id': 'cid', 'client_secret': 'csec'})
        endpoints.token = TestGerencianet.auth_success
        response = endpoints.create_charge(body = {'items': items})

        assert response == TestGerencianet.charge

    @responses.activate
    def test_api_request_call_with_partner_token(self):
        responses.add(responses.POST, Constants.URL['sandbox'] + '/authorize',
                      content_type='application/json', status=200,
                      json=TestGerencianet.auth_success)

        responses.add(responses.POST, Constants.URL['sandbox'] + '/charge',
                      content_type='application/json', status=200,
                      json=TestGerencianet.charge)

        items = [
            {'name': 'item 1', 'value': 1000},
            {'name': 'item 2', 'value': 2000}
        ]

        endpoints = Gerencianet({'client_id': 'cid', 'client_secret': 'csec', 'partner_token': 'partner'})
        response = endpoints.create_charge(body={'items': items})

        assert response == TestGerencianet.charge
