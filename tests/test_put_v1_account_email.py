import structlog
from dm_api_account.models.change_email_model import ChangeEmail
from hamcrest import assert_that, has_properties
from services.dm_api_account import Facade
from generic.helpers.mailhog import MailhogApi
from dm_api_account.models.user_envelope_model import UserRole
from dm_api_account.models.user_envelope_model import Rating


structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    api = Facade(host='http://5.63.153.31:5051')

    login = "some1313"
    email = "some1313@gmail.com"
    password = "some61234"

    # Register new user
    api.account.register_new_user(login=login, email=email, password=password)
    # Activate new user
    api.account.activate_registered_user(login=login)
    # Login new user
    api.login.login_new_user(login=login, password=password)

    json = ChangeEmail(login="some1313", email="some1313@gmail.com", password="some61234")
    response = api.account_api.put_v1_account_email(json=json)

    assert_that(response.resource, has_properties(
        {
            "login": "some1313",
            "roles": [UserRole.guest, UserRole.player],
            "rating": Rating(enabled=True, quality=0, quantity=0)

        }
    ))
    #done