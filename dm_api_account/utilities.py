import requests
from pydantic import BaseModel


def validate_request_json(json: str | BaseModel):
    if isinstance(json, dict):
        return json
    return json.dict(by_alias=True, exclude_none=True)


def validate_status_code(response: requests.Response, status_code: int):
    """

    :rtype: object
    """
    assert response.status_code == status_code, \
        f'Статус код ответа должен быть равен 201, но он равен {response.status_code}'
