import structlog
from dm_api_account.models.change_email_model import ChangeEmail
from hamcrest import assert_that, has_properties
from services.dm_api_account import DmApiAccount
from services.mailhog import MailhogApi
from dm_api_account.models.user_envelope_model import UserRole
from dm_api_account.models.user_envelope_model import Rating

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    mailhog = MailhogApi(host='http://5.63.153.31:5025')
    api = DmApiAccount(host='http://5.63.153.31:5051')

    json = ChangeEmail(login="some012", email="some0122@gmail.com", password="some61234")
    response = api.account.put_v1_account_email(json=json)

    assert_that(response.resource, has_properties(
        {
            "login": "some012",
            "roles": [UserRole.guest, UserRole.player],
            "rating": Rating(enabled=True, quality=0, quantity=0)

        }
    ))
