import requests

"""
Logout from every device
"""


def delete_v1_account_login_all():
    url = "http://5.63.153.31:5051/v1/account/login/all"

    headers = {
        'X-Dm-Auth-Token': '<string>',
        'X-Dm-Bb-Render-Mode': '<string>',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="DELETE",
        url=url,
        headers=headers,
        json=payload
    )

    return response
