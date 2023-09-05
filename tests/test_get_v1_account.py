from services.dm_api_account import DmApiAccount
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_details_envelope import UserRole
from dm_api_account.models.user_details_envelope import Rating
from dm_api_account.models.login_credentials_model import LoginCredentials
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_get_v1_account():
    api = DmApiAccount(host='http://5.63.153.31:5051')
    # json = LoginCredentials(login="some108", rememberMe=True, password="some61234")
    # response = api.login.post_v1_account_login(json=json)
    # assert response.status_code == 200, f'Статус код ответа должен быть равен 200, но он равен {response.status_code}'
    headers = {

        'X-Dm-Auth-Token': 'IQJh+zgzF5ApjfvOQPcj0LVJaFGTKRFBJOFF299skvKmDu+M3F2Svyw+NTNeUROExyJegl0Md1W9udFs0+IoqrruqTFPs7GNcIPKw4e9dcpM7lUWl00PdIhaR1YECywW3Xg043Ji6PM='
    }
    response = api.account.get_v1_account(headers=headers)

    assert_that(response.resource, has_properties(
        {
            "info": "",
            "login": "some012",
            "roles": [UserRole.guest, UserRole.player],
            "rating": Rating(enabled=True, quality=0, quantity=0)

        }
    ))
