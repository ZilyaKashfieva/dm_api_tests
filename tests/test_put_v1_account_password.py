from dm_api_account.models.change_account_password import ChangePassword
from hamcrest import assert_that, has_properties
from services.dm_api_account import DmApiAccount
from dm_api_account.models.user_envelope_model import UserRole
from dm_api_account.models.user_envelope_model import Rating
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    api = DmApiAccount(host='http://5.63.153.31:5051')

    json = ChangePassword(
        login="some009", token="a64dba5a-f826-48c7-a2dc-a76f466ef4bd", oldPassword="some612345",
        newPassword="some6123456"
    )
    response = api.account.put_v1_account_password(json=json)
    assert_that(response.resource, has_properties(
        {

            "login": "some009",
            "roles": [UserRole.guest, UserRole.player],
            "rating": Rating(enabled=True, quality=0, quantity=0)

        }
    ))
