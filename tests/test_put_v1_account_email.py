import structlog
from dm_api_account.models.change_email_model import ChangeEmail
from hamcrest import assert_that, has_properties
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
from dm_api_account.models.user_envelope_model import UserRole
from dm_api_account.models.user_envelope_model import Rating
from dm_api_account.models.registration_model import Registration
from dm_api_account.models.login_credentials_model import LoginCredentials

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    mailhog = MailhogApi(host='http://5.63.153.31:5025')

    json = Registration(login="some613", email="some613@gmail.com", password="some61234")
    response = api.account.post_v1_account(json=json)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    json = LoginCredentials(login="some613", rememberMe=True, password="some61234")
    response = api.login.post_v1_account_login(json=json)

    json = ChangeEmail(login="some613", email="some6135@gmail.com", password="some61234")
    response = api.account.put_v1_account_email(json=json)

    assert_that(response.resource, has_properties(
        {
            "login": "some613",
            "roles": [UserRole.guest, UserRole.player],
            "rating": Rating(enabled=True, quality=0, quantity=0)

        }
    ))
