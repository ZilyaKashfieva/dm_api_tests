import requests
import json

"""
Register new user
"""


def post_v1_account():
    url = "http://5.63.153.31:5051/v1/account"

    payload = {
        "login": "some5",
        "email": "some5@gmail.com",
        "password": "some61234"
    }
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


response = post_v1_account()
print(response.request)
print(response.content)
print(response.url)
print(response.status_code)
print(response.json()['type'])
print(response.json()['title'])
print(response.request.url)
print(response.request.body)
print(response.request.method)
print(response.request.headers)
