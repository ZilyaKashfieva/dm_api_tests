import structlog
from dm_api_account.models.change_email_model import ChangeEmail
from hamcrest import assert_that, has_properties
from services.dm_api_account import Facade
from generic.helpers.mailhog import MailhogApi
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
    api = Facade(host='http://5.63.153.31:5051')

    login = "some133"
    email = "some133@gmail.com"
    password = "some61234"

    # Register new user
    response = api.account.register_new_user(login=login, email=email, password=password)
    # Activate new user
    api.account.activate_registered_user(login=login)
    # Login new user
    response = api.login.login_new_user(login=login, password=password)

    response = api.account_api.put_v1_account_email(login="some613", email="some6135@gmail.com", password="some61234")

    assert_that(response.resource, has_properties(
        {
            "login": "some613",
            "roles": [UserRole.guest, UserRole.player],
            "rating": Rating(enabled=True, quality=0, quantity=0)

        }
    ))
