import requests
import json

"""
Change registered user email
"""


def put_v1_account_email():
    url = "http://5.63.153.31:5051/v1/account/email"

    payload = json.dumps({
        "login": "<string>",
        "password": "<string>",
        "email": "<string>"
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