import structlog
from services.dm_api_account import DmApiAccount
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
    api = DmApiAccount(host='http://5.63.153.31:5051')

    # json = Registration(login="some108", email="some108@gmail.com", password="some61234")
    # response = api.account.post_v1_account(json=json)
    # assert response.status_code == 201, f'Статус код ответа должен быть равен 201, но он равен {response.status_code}'
    # token = mailhog.get_token_from_last_email()
    # response = api.account.put_v1_account_token(token=token)
    # assert response.status_code == 200, f'Статус код ответа должен быть равен 200, но он равен {response.status_code}'
    json = LoginCredentials(login="some012", rememberMe=True, password="some61234")
    response = api.login.post_v1_account_login(json=json)
    assert_that(response.resource, has_properties(
        {
            "login": "some012",
            "roles": [UserRole.guest, UserRole.player],
            "rating": Rating(enabled=True, quality=0, quantity=0)

        }
    ))
