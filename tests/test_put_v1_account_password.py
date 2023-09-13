from dm_api_account.models.change_account_password import ChangePassword
from hamcrest import assert_that, has_properties
from services.dm_api_account import Facade
from dm_api_account.models.user_envelope_model import UserRole
from dm_api_account.models.user_envelope_model import Rating
from generic.helpers.mailhog import MailhogApi
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_password():
    api = Facade(host='http://5.63.153.31:5051')
    login = "some171"
    email = "some171@gmail.com"
    password = "some61234"
    oldPassword = "some61234"
    newPassword = "some612345"

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
    api.account.reset_password(login=login, email=email)

    #  Change password
    response = api.account.change_password(login=login, oldPassword=oldPassword, newPassword=newPassword)

    assert_that(response.resource, has_properties(
        {

            "login": "some171",
            "roles": [UserRole.guest, UserRole.player],
            "rating": Rating(enabled=True, quality=0, quantity=0)

        }
    ))
    #done