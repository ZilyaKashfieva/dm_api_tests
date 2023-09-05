from hamcrest import assert_that, has_properties
from dm_api_account.models.reset_password_model import ResetPassword
from services.dm_api_account import DmApiAccount
from dm_api_account.models.user_envelope_model import UserRole
from dm_api_account.models.user_envelope_model import Rating
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_password():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    json = ResetPassword(login="some009", email="some009@gmail.com")
    response = api.account.post_v1_account_password(json=json)
    assert_that(response.resource, has_properties(
        {

            "login": "some009",
            "roles": [UserRole.guest, UserRole.player],
            "rating": Rating(enabled=True, quality=0, quantity=0)

        }
    ))
