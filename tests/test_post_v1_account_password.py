from dm_api_account.models.reset_password_model import ResetPassword
import structlog
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
from dm_api_account.models.login_credentials_model import LoginCredentials
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole
from dm_api_account.models.user_envelope_model import Rating
from dm_api_account.models.registration_model import Registration

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_password():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    json = Registration(login="some314", email="some314@gmail.com", password="some61234")
    response = api.account.post_v1_account(json=json)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    json = LoginCredentials(login="some314", rememberMe=True, password="some61234")
    response = api.login.post_v1_account_login(json=json)

    json = ResetPassword(login="some314", email="some314@gmail.com")
    response = api.account.post_v1_account_password(json=json)
    assert_that(response.resource, has_properties(
        {

            "login": "some314",
            "roles": [UserRole.guest, UserRole.player],
            "rating": Rating(enabled=True, quality=0, quantity=0)

        }
    ))
