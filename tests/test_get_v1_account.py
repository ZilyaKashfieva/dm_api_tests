import time

from services.dm_api_account import Facade
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_details_envelope import UserRole
from dm_api_account.models.user_details_envelope import Rating
import structlog
from generic.helpers.mailhog import MailhogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_get_v1_account():
    api = Facade(host='http://5.63.153.31:5051')
    login = "some132"
    email = "some132@gmail.com"
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

    # assert_that(response.resource, has_properties(
    #     {
    #         "info": "",
    #         "login": "some012",
    #         "roles": [UserRole.guest, UserRole.player],
    #         "rating": Rating(enabled=True, quality=0, quantity=0)
    #
    #     }
    # ))
