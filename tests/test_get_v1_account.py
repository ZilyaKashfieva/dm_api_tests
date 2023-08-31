import requests

from dm_api_account.models.login_credentials_model import LoginCredentialsModel
from services.dm_api_account import DmApiAccount


def test_get_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')

    # json = LoginCredentialsModel(login="some108", rememberMe=True, password="some61234")
    # response = api.login.post_v1_account_login(json=json)
    # assert response.status_code == 200, f'Статус код ответа должен быть равен 200, но он равен {response.status_code}'
    headers = {

        'X-Dm-Auth-Token': 'IQJh+zgzF5A9TLAzuPUVjn7GYXC2AmzhNmd4sp8dR3PIBPWHcvOrZXp+M+Fg4H1NsHuo9evAbBtcJ5iT9qZzyiEnQqoGkIztwbF0EzvuHXrbV3KLNuiVMzqEUF99LtSSYs/2riDt1M8='
    }
    response = api.account.get_v1_account(headers=headers)
