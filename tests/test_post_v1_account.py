import structlog
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
from dm_api_account.models.registration_model import Registration
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole
from dm_api_account.models.user_envelope_model import Rating

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')

    json = Registration(login="some113", email="some113@gmail.com", password="some61234")
    response = api.account.post_v1_account(json=json)
    token = mailhog.get_token_from_last_email()
    response = api.account.put_v1_account_token(token=token)
    assert_that(response.resource, has_properties(
        {
            "login": "some113",
            "roles": [UserRole.guest, UserRole.player],
            "rating": Rating(enabled=True, quality=0, quantity=0)

        }
    ))
