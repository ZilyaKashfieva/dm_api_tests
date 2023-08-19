import requests
import json
from services.dm_api_account import DmApiAccount


def test_put_v1_account_email():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = {
        "login": "some6",
        "password": "some61234",
        "email": "some6@gmail.com"

    }
    response = api.account.put_v1_account_email(
        json=json
    )
    print(response)
