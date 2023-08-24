import requests.exceptions
from requests import session, Response
import structlog
import uuid
import curlify


class Restclient:
    def __init__(self, host, headers=None):
        self.host = host
        self.session = session()
        if headers:
            self.session.headers.update(headers)
        self.log = structlog.get_logger(self.__class__.__name__).bind(service='api')

    def post(self, path: str, **kwargs) -> Response:
        return self._send_request('POST', path, **kwargs)

    def get(self, path: str, **kwargs) -> Response:
        return self._send_request('GET', path, **kwargs)

    def put(self, path: str, **kwargs) -> Response:
        return self._send_request('PUT', path, **kwargs)

    def _send_request(self, method, path, **kwargs):
        full_url = self.host + path
        log = self.log.bind(event_id=str(uuid.uuid4()))
        log.msg(
            event='request',
            method=method,
            full_url=full_url,
            params=kwargs.get('params'),
            headers=kwargs.get('headers'),
            json=kwargs.get('json'),
            data=kwargs.get('data'),

        )

        response = self.session.request(
            method=method,
            url=full_url,
            **kwargs

        )

        curl = curlify.to_curl(response.request)
        print(curl)
        log.msg(
            event='response',
            status=Response.status_code,
            headers=Response.headers,
            json=self._get_json(response),
            text=Response.text,
            content=Response.content,
            curl=curl
        )
        return response

    def _get_json(response):
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return