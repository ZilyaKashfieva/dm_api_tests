from requests import Response
from restclient.restclient import Restclient
from ..models.change_account_password import change_account_password
from ..models.change_email_model import ChangeEmailModel
from ..models.registration_model import RegistrationModel
from ..models.reset_password_model import reset_password_model
from dm_api_account.models.user_envelope_model import UserEnvelopeModel


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.client = Restclient(host=host, headers=headers)
        if headers:
            self.client.session.headers.update(headers)

    def post_v1_account(self, json: RegistrationModel, **kwargs) -> Response:
        """
        :param json registration_model
        Register new user
        :return
        """

        response = self.client.post(
            path=f"/v1/account",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs

        )
        return response

    def post_v1_account_password(self, json: reset_password_model, **kwargs) -> Response:
        """
        :param json reset_password_model
        Reset registered user password
        :return
        """

        response = self.client.post(
            path=f"/v1/account/password",
            json=json,
            **kwargs
        )

        return response

    def get_v1_account(self, **kwargs):
        """
        Get current user
        :return
        """

        response = self.client.get(
            path=f"/v1/account",
            **kwargs

        )

        return response

    def put_v1_account_email(self, json: ChangeEmailModel, **kwargs) -> Response:
        """
        :param json change_email_model
        Change registered user email
        :return
        """

        response = self.client.put(
            path=f"/v1/account/email",
            json=json.model_dump(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_password(self, json: change_account_password, **kwargs) -> Response:
        """
        :param json change_account_password
        Change registered user password
        :return
        """

        response = self.client.put(
            path=f"/v1/account/password",
            json=json,
            **kwargs
        )

        return response

    def put_v1_account_token(self, token: str, **kwargs) -> Response:
        """
        :param token:
        Activate registered user
        :return
        """

        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response
