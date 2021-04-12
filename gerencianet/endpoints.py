# encoding: utf-8

from __future__ import unicode_literals
from six import iteritems

import json
import re
import requests
import inspect
import base64

from .constants import Constants
from .exceptions import MissingParametersError
from .exceptions import UnauthorizedError
from .version import *

from functools import partial

class Endpoints(object):

    def __init__(self, options):
        super(Endpoints, self).__init__()
        self.token = None
        self.options = options

    def __getattr__(self, name):
        if name in Constants.ENDPOINTS['PIX']:
            self.endpoints = Constants.ENDPOINTS['PIX']
            self.urls = Constants.URL['PIX']
        else:
            self.endpoints = Constants.ENDPOINTS['DEFAULT']
            self.urls = Constants.URL['DEFAULT']
            self.options['pix_cert'] = None
        self.get_url()
        return partial( self.request, self.endpoints[name])

    def request(self, settings, **kwargs):

        self.authenticate()
        
        params = {} if 'params' not in kwargs else kwargs['params']
        body = {} if 'body' not in kwargs else kwargs['body']
        headers = {} if 'headers' not in kwargs else kwargs['headers']

        response = self.send(settings, params, body, headers)

        try:
        	response.json()
        except:
        	return '{\'code\': ' + str(response.status_code) + '}'
        else:
        	return response.json()

    def send(self, settings, params, body, headersComplement):
        url = self.build_url(settings['route'], params)

        if(self.options['pix_cert']):
            headers = {
                'Authorization': 'Bearer {token}'.format(token=self.token['access_token']),
                'Content-Type': 'application/json',
                'api-sdk': 'python-{v}'.format(v=VERSION)
            }

            for (key,value) in headersComplement.items():
                headers[key] = value

            if 'partner_token' in self.options:
                headers['partner-token'] = self.options['partner_token']
            cert=self.options['pix_cert']
            return requests.request(settings['method'],url, headers=headers, data=json.dumps(body), cert=cert)
        else:
            headers = {
                'accept': 'application/json',
                'api-sdk': 'python-{v}'.format(v=VERSION),
                'Authorization': 'Bearer {token}'.format(token=self.token['access_token'])
            }
            if 'partner_token' in self.options:
                headers['partner-token'] = self.options['partner_token']
            return requests.request(settings['method'], url, json=body, headers=headers)

    def authenticate(self):
        
        url = self.build_url(self.endpoints['authorize']['route'], {})             
        
        if(self.options['pix_cert']):
            auth = base64.b64encode((f"{self.options['client_id']}:{self.options['client_secret']}").encode()).decode()
            payload = "{\r\n    \"grant_type\": \"client_credentials\"\r\n}"
            headers = {
                'Authorization': f"Basic {auth}",
                'Content-Type': 'application/json'
            }
            if 'partner_token' in self.options:
                headers['partner-token'] = self.options['partner_token']
            cert=self.options['pix_cert']
            response = requests.post(url, headers=headers, data=payload, cert=cert)
        else:
            headers = {
                'accept': 'application/json',
                'api-sdk': 'python-{v}'.format(v=VERSION)
            }
            if 'partner_token' in self.options:
                headers['partner-token'] = self.options['partner_token']
            auth = (self.options['client_id'], self.options['client_secret'])
            auth_body =  {'grant_type': 'client_credentials'}
            response = requests.post(url, headers=headers, auth=auth, json=auth_body)

        if response.status_code == 200:
            json =  response.json()
            self.token = json
        else:
            raise UnauthorizedError(response.status_code)

    def get_url(self):
        self.base_url = self.urls['sandbox']
        if 'sandbox' in self.options:
            self.base_url = self.urls['sandbox'] if self.options[
                'sandbox'] else self.urls['production']

    def build_url(self, route, params):
        params = {} if params is None else params
        route = self.remove_placeholders(route, params)
        return self.complete_url(route, params)

    def remove_placeholders(self, route, params):
        regex = r'\:(\w+)'
        match = re.findall(regex, route)
        if match:
            for attr in match:
                if attr not in params:
                    raise MissingParametersError(attr)
                route = route.replace(':' + attr, str(params[attr]))
                del params[attr]

        return route


    def query_string(self, params):
        mapped = []
        for (p, value) in iteritems(params):
            mapped.append('{attr}={value}'.format(attr=p, value=value))
        return '&'.join(mapped)

    def complete_url(self, route, params):
        qs = self.query_string(params)

        if len(qs) == 0:
            return '{base}{route}'.format(base=self.base_url, route=route)

        return '{base}{route}?{qs}'.format(base=self.base_url, route=route, qs=qs)
