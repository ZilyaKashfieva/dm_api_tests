import structlog
from services.dm_api_account import DmApiAccount
import json
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole
from dm_api_account.models.user_envelope_model import Rating

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    response = api.account.put_v1_account_token(token='7fd5d239-7e29-4c6a-be4d-44943596796b')
    assert_that(response.resource, has_properties(
        {
            "login": "some012",
            "roles": [UserRole.guest, UserRole.player],
            "rating": Rating(enabled=True, quality=0, quantity=0)

        }
    ))
