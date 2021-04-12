# encoding: utf-8


class Constants(object):
    URL = {
        'DEFAULT': {
            'production': 'https://api.gerencianet.com.br/v1',
            'sandbox': 'https://sandbox.gerencianet.com.br/v1'
        },
        'PIX': {
            'production': 'https://api-pix.gerencianet.com.br',
            'sandbox': 'https://api-pix-h.gerencianet.com.br'
        }
    }

    ENDPOINTS = {
        'DEFAULT': {
            'authorize': {
                'route': '/authorize',
                'method': 'post'
            },
            'create_charge': {
                'route': '/charge',
                'method': 'post'
            },
            'detail_charge': {
                'route': '/charge/:id',
                'method': 'get'
            },
            'update_charge_metadata': {
                'route': '/charge/:id/metadata',
                'method': 'put'
            },
            'update_billet': {
                'route': '/charge/:id/billet',
                'method': 'put'
            },
            'pay_charge': {
                'route': '/charge/:id/pay',
                'method': 'post'
            },
            'cancel_charge': {
                'route': '/charge/:id/cancel',
                'method': 'put'
            },
            'create_carnet': {
                'route': '/carnet',
                'method': 'post'
            },
            'detail_carnet': {
                'route': '/carnet/:id',
                'method': 'get'
            },
            'update_parcel': {
                'route': '/carnet/:id/parcel/:parcel',
                'method': 'put'
            },
            'update_carnet_metadata': {
                'route': '/carnet/:id/metadata',
                'method': 'put'
            },
            'get_notification': {
                'route': '/notification/:token',
                'method': 'get'
            },
            'get_plans': {
                'route': '/plans',
                'method': 'get'
            },
            'create_plan': {
                'route': '/plan',
                'method': 'post'
            },
            'delete_plan': {
                'route': '/plan/:id',
                'method': 'delete'
            },
            'create_subscription': {
                'route': '/plan/:id/subscription',
                'method': 'post'
            },
            'detail_subscription': {
                'route': '/subscription/:id',
                'method': 'get'
            },
            'pay_subscription': {
                'route': '/subscription/:id/pay',
                'method': 'post'
            },
            'cancel_subscription': {
                'route': '/subscription/:id/cancel',
                'method': 'put'
            },
            'update_subscription_metadata': {
                'route': '/subscription/:id/metadata',
                'method': 'put'
            },
            'get_installments': {
                'route': '/installments',
                'method': 'get'
            },
            'resend_billet': {
                'route': '/charge/:id/billet/resend',
                'method': 'post'
            },
            'create_charge_history': {
                'route': '/charge/:id/history',
                'method': 'post'
            },
            'create_charge_onestep': {
                'route': '/charge/one-step',
                'method': 'post'
            },
            'resend_carnet': {
                'route': '/carnet/:id/resend',
                'method': 'post'
            },
            'resend_parcel': {
                'route': '/carnet/:id/parcel/:parcel/resend',
                'method': 'post'
            },
            'create_carnet_history': {
                'route': '/carnet/:id/history',
                'method': 'post'
            },
            'cancel_carnet': {
                'route': '/carnet/:id/cancel',
                'method': 'put'
            },
            'cancel_parcel': {
                'route': '/carnet/:id/parcel/:parcel/cancel',
                'method': 'put'
            },
            'link_charge': {
                'route': '/charge/:id/link',
                'method': 'post'
            },
            'charge_link': {
                'route': '/charge/:id/link',
                'method': 'post'
            },
            'update_charge_link': {
                'route': '/charge/:id/link',
                'method': 'put'
            },
            'update_plan': {
                'route': '/plan/:id',
                'method': 'put'
            },
            'create_subscription_history': {
                'route': '/subscription/:id/history',
                'method': 'post'
            },
            'create_charge_balance_sheet': {
                'route': '/charge/:id/balance_sheet',
                'method': 'post'
            },
            'settle_charge': {
                'route': '/charge/:id/settle',
                'method': 'put'
            },
            'settle_carnet_parcel': {
                'route': '/carnet/:id/parcel/:parcel/settle',
                'method': 'put'
            }
        },
        'PIX': {
            "authorize": {
                "route": "/oauth/token",
                "method": "post"
            },
            "pix_config_webhook": {
                "route": "/v2/webhook/:chave",
                "method": "put"
            },
            "pix_get_webhook": {
                "route": "/v2/webhook/:chave",
                "method": "get"
            },
            "pix_list_webhook": {
                "route": "/v2/webhook",
                "method": "get"
            },
            "pix_delete_webhook": {
                "route": "/v2/webhook/:chave",
                "method": "delete"
            },
            "pix_create_charge": {
                "route": "/v2/cob/:txid",
                "method": "put"
            },
            "pix_create_immediate_charge": {
                "route": "/v2/cob",
                "method": "post"
            },
            "pix_detail_charge": {
                "route": "/v2/cob/:txid",
                "method": "get"
            },
            "pix_update_charge": {
                "route": "/v2/cob/:txid",
                "method": "patch"
            },
            "pix_list_charges": {
                "route": "/v2/cob",
                "method": "get"
            },
            "pix_generate_QRCode": {
                "route": "/v2/loc/:id/qrcode",
                "method": "get"
            },
            "pix_devolution": {
                "route": "/v2/pix/:e2eId/devolucao/:id",
                "method": "put"
            },
            "pix_devolution_get": {
                "route": "/v2/pix/:e2eId/devolucao/:id",
                "method": "get"
            },
            "pix_send": {
                "route": "/v2/pix",
                "method": "post"
            },
            "pix_send_list": {
                "route": "/v2/pix/:e2eId",
                "method": "get"
            },
            "pix_received_list": {
                "route": "/v2/pix",
                "method": "get"
            },
            "pix_location_create": {
                "route": "/v2/loc",
                "method": "post"
            },
            "pix_location_list": {
                "route": "/v2/loc",
                "method": "get"
            },
            "pix_location_get": {
                "route": "/v2/loc/:id",
                "method": "get"
            },
            "pix_location_delete_txid": {
                "route": "/v2/loc/:id/txid",
                "method": "delete"
            },
            "pix_create_evp": {
                "route": "/v2/gn/evp",
                "method": "post"
            },
            "pix_list_evp": {
                "route": "/v2/gn/evp",
                "method": "get"
            },
            "pix_delete_evp": {
                "route": "/v2/gn/evp/:chave",
                "method": "delete"
            },
            "pix_list_balance": {
                "route": "/v2/gn/saldo",
                "method": "get"
            },
            "pix_update_settings": {
                "route": "/v2/gn/config",
                "method": "put"
            },
            "pix_list_settings": {
                "route": "/v2/gn/config",
                "method": "get"
            }
        }
    }