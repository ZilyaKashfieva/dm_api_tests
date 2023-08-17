import requests
import json

"""
Change registered user password
"""


def put_v1_account_password():
    url = "http://5.63.153.31:5051/v1/account/password"

    payload = json.dumps({
        "login": "<string>",
        "token": "<uuid>",
        "oldPassword": "<string>",
        "newPassword": "<string>"
    })
    headers = {
        'X-Dm-Auth-Token': '<string>',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="PUT",
        url=url,
        headers=headers,
        json=payload
    )

    return response
