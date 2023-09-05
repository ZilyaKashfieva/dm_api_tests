from __future__ import annotations
from typing import Any, Dict, List, Optional
from uuid import UUID
from pydantic import BaseModel, Extra, Field, StrictBool


class ChangePassword(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[str] = Field(None, description='User login')
    token: Optional[str] = Field(None, description='Password reset token')
    old_password: Optional[str] = Field(
        None, alias='oldPassword', description='Old password'
    )
    new_password: Optional[str] = Field(
        None, alias='newPassword', description='New password'
    )
