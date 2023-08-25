import structlog
import json
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    mailhog = MailhogApi(host='http://5.63.153.31:5025/api')
    api = DmApiAccount(host='http://5.63.153.31:5051')

    json = dict(login="some32", email="some32@gmail.com", password="some61234")
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'Статус код ответа должен быть равен 201, но он равен {response.status_code}'
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    assert response.status_code == 200, f'Статус код ответа должен быть равен 200, но он равен {response.status_code}'
    json = dict(login="some32", rememberMe=True, password="some61234")
    response = api.login.post_v1_account_login(json=json)
    assert response.status_code == 200, f'Статус код ответа должен быть равен 200, но он равен {response.status_code}'
