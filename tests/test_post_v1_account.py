import structlog
import json
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
from dm_api_account.models.registration_model import RegistrationModel

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = MailhogApi(host='http://5.63.153.31:5025/api')
    api = DmApiAccount(host='http://5.63.153.31:5051')

    json = RegistrationModel(login="some003", email="some003@gmail.com", password="some61234")
    response = api.account.post_v1_account(json=json)
    assert response.status_code == 201, f'Статус код ответа должен быть равен 201, но он равен {response.status_code}'
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    assert response.status_code == 200, f'Статус код ответа должен быть равен 200, но он равен {response.status_code}'
