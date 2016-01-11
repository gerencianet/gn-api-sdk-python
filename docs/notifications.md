## Notifications

Any changes that happen in the charges will trigger an event that notifies the `notification_url` provided at creation time (see [creating charges](/docs/charges.md)).

It's also possible to set or change the `notification_url` for existing charges, see [updating informations](/docs/charge-update.md).

Given that a charge has a valid `notification_url`, when the notification time comes you'll receive a post with a `token`. This token must be used to get the notification payload data.

The example below assumes that you're using any routing app. It's easier showing than explaining with words:

```python
  # supposing that this is a post route
  def notification_route(self, notification):
      params = {
        'token': notification
      }

      response =  gn.get_notification(params=params)

      #do something with the response, like updating your transaction status
      #storing on db, or anything else

```

The response will look with something like:

```python
{
  "code": 200,
  "data": [{
    "id": 1,
    "type": "charge",
    "custom_id": None,
    "status": {
      "current": "new",
      "previous": None
    },
    "identifiers": {
      "charge_id": 1002
    }
  }, {
    "id": 2,
    "type": "charge",
    "custom_id": None,
    "status": {
      "current": "waiting",
      "previous": "new"
    },
    "identifiers": {
      "charge_id": 1002
    }
  }, {
    "id": 3,
    "type": "charge",
    "custom_id": None,
    "status": {
      "current": "paid",
      "previous": "waiting"
    },
    "identifiers": {
      "charge_id": 1002
    },
    "value": 2000
  }, {
    "id": 4,
    "type": "charge",
    "custom_id": None,
    "status": {
      "current": "refunded",
      "previous": "paid"
    },
    "identifiers": {
      "charge_id": 1002
    }
  }]
}
```

The response will be an array with all the changes of a certain token that happened within the past 6 months. It will have the following parameters:

* id: Each notification has its own sequence, starting from `1`. The `id` parameter identifies this sequence. This is useful if you need to keep track of what changes you have already processed.

* type: Available values are:
  * `charge` - a charge have changed
  * `subscription` - a subscription have changed
  * `carnet` - a carnet have changed
  * `subscription_charge` - one subscription's parcel have changed
  * `carnet_charge` - one carnet's parcel have changed

* custom_id: your custom_id.

* status: Contains the `current` and `previous` (before the change) status  of the transaction.

 p.s.: if there is no `previous` status (i.e.: for new charges), the `previous` value will be None.

* identifiers: Identifiers related to the change. It may have one or more identifier, depending on the type:
  * for `charge` type: identifiers will contain only `charge_id`.
  * for `subscription` type: identifiers will contain only `subscription_id`.
  * for `carnet` type: identifiers will contain only `carnet_id`.
  * for `subscription_charge` type: identifiers will contain both `charge_id` and `subscription_id`.
  * for `carnet_charge` type: identifiers will contain both `charge_id` and `carnet_id`.

* value: This parameter will only be shown when the status changes to paid.

 For more informations about notifications, please refer to [Gerencianet](https://docs.gerencianet.com.br/#!/charges/notifications).
