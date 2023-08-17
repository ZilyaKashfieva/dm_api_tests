import requests

"""
Activate registered user
"""


def put_v1_account_token():
    token = 'ghdfdf'
    url = "http://5.63.153.31:5051/v1/account/{token}"

    headers = {
        'X-Dm-Auth-Token': '<string>',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Accept': 'text/plain'
    }

    response = requests.request(
        metod="PUT",
        url=url,
        headers=headers,
        json=payload
    )

    return response
