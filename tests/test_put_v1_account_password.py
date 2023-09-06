from dm_api_account.models.change_account_password import ChangePassword
from hamcrest import assert_that, has_properties
from services.dm_api_account import DmApiAccount
from dm_api_account.models.user_envelope_model import UserRole
from dm_api_account.models.user_envelope_model import Rating
from services.mailhog import MailhogApi
from dm_api_account.models.registration_model import Registration
from dm_api_account.models.login_credentials_model import LoginCredentials
from dm_api_account.models.reset_password_model import ResetPassword
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    mailhog = MailhogApi(host='http://5.63.153.31:5025')

    # json = Registration(login="some515", email="some515@gmail.com", password="some61234")
    # response = api.account.post_v1_account(json=json)
    # token = mailhog.get_token_from_last_email()
    # response = api.account.put_v1_account_token(token=token)
    # json = LoginCredentials(login="some515", rememberMe=True, password="some61234")
    # response = api.login.post_v1_account_login(json=json)
    # json = ResetPassword(login="some515", email="some515@gmail.com")
    # response = api.account.post_v1_account_password(json=json)
    json = ChangePassword(
        login="some515",
        token="f1706907-744e-43f3-a81c-1c286798a6e7",
        oldPassword="some61234",
        newPassword="some6123456"
    )

    response = api.account.put_v1_account_password(json=json)
    assert_that(response.resource, has_properties(
        {

            "login": "some515",
            "roles": [UserRole.guest, UserRole.player],
            "rating": Rating(enabled=True, quality=0, quantity=0)

        }
    ))
