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


def test_post_v1_account_login():
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

    # assert_that(response.resource, has_properties(
    #     {
    #         "login": "some124",
    #         "roles": [UserRole.guest, UserRole.player],
    #         "rating": Rating(enabled=True, quality=0, quantity=0)
    #
    #     }
    # ))
