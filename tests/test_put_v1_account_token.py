from services.dm_api_account import DmApiAccount
def test_put_v1_account_token():
    api = DmApiAccount(host='http://5.63.153.31:5051')



    response = api.account.put_v1_account_token(
        token= '3fa85f64-5717-4562-b3fc-2c963f66afa6'

    )
    print(response)




