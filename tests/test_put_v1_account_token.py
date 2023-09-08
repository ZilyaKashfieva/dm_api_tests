import structlog
from services.dm_api_account import Facade
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole
from dm_api_account.models.user_envelope_model import Rating
from generic.helpers.mailhog import MailhogApi
from dm_api_account.models.registration_model import Registration

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = Facade(host='http://5.63.153.31:5051')
    login = "some150"
    email = "some150@gmail.com"
    password = "some61234"

    # Register new user
    api.account.register_new_user(login=login, email=email, password=password)
    # Activate new user
    api.account.activate_registered_user(login=login)
    # assert_that(response.resource, has_properties(
    #     {
    #         "login": "some014",
    #         "roles": [UserRole.guest, UserRole.player],
    #         "rating": Rating(enabled=True, quality=0, quantity=0)
    #
    #     }
    # ))
