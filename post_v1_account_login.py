import requests
import json

"""
Authenticate via credentials
"""


def pos_v1_account_login():
    url = "http://5.63.153.31:5051/v1/account/login"

    payload = {
        "login": "<string>",
        "password": "<string>",
        "rememberMe": "<boolean>"
    }
    headers = {
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
