import requests
import json

"""
Reset registered user password
"""


def post_v1_account_password():
    url = "http://5.63.153.31:5051/v1/account/password"

    payload = json.dumps({
        "login": "<string>",
        "email": "<string>"
    })
    headers = {
        'X-Dm-Auth-Token': '<string>',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="POST",
        url=url,
        headers=headers,
        json=payload
    )

    return response
