from pydantic import BaseModel, StrictStr


class ChangeAccountPassword(BaseModel):
    login: StrictStr
    token: StrictStr
    oldPassword: StrictStr
    newPassword: StrictStr
