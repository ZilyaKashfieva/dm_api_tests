import requests
from services.dm_api_account import DmApiAccount
def test_post_v1_account(cookies=None):
    api = DmApiAccount(host='http://5.63.153.31:5051')

    json = {
        "login": "some12",
        "email": "some12@gmail.com",
        "password": "some61234"
    }
    response = api.account.post_v1_account(
        json=json

    )
    print(response)





