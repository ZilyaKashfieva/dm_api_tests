from services.dm_api_account import DmApiAccount
def test_put_v1_account_token():
    api = DmApiAccount(host='http://5.63.153.31:5051')



    response = api.account.put_v1_account_token(
        token= '23ed557f-a65d-40d8-aad2-453a3e772379'

    )
    print(response)




