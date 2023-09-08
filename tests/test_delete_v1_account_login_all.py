from services.dm_api_account import Facade


def test_delete_v1_account_login_all():
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
    # Logout user from all devices
    api.login.logout_user_from_all()
