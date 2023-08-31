import json
import requests

from dm_api_account.models.reset_password_model import ResetPasswordModel
from services.dm_api_account import DmApiAccount


def test_post_v1_account_password():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = ResetPasswordModel(login="some403", email="some403@gmail.com")
    response = api.account.post_v1_account_password(json=json)
    print(response)
