from dm_api_account.models.reset_password_model import ResetPassword
import structlog
from services.dm_api_account import Facade
from generic.helpers.mailhog import MailhogApi
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
    api = Facade(host='http://5.63.153.31:5051')
    login = "some1509"
    email = "some1509@gmail.com"
    password = "some61234"

    # Register new user
    api.account.register_new_user(login=login, email=email, password=password)
    # Activate new user
    api.account.activate_registered_user(login=login)
    # Login new user
    api.login.login_new_user(login=login, password=password)

    token = api.login.get_auth_token(login=login, password=password)
    api.account.set_headers(headers=token)
    api.login.set_headers(headers=token)

    # Get current user
    api.account.get_current_user_info()
    # Reset password
    response = api.account.reset_password(login=login, email=email)

    assert_that(response.resource, has_properties(
        {

            "login": "some1509",
            "roles": [UserRole.guest, UserRole.player],
            "rating": Rating(enabled=True, quality=0, quantity=0)

        }
    ))
    #done
