from __future__ import annotations
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Extra, Field, StrictBool


class ChangeEmail(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[str] = Field(None, description='User login')
    password: Optional[str] = Field(None, description='User password')
    email: Optional[str] = Field(None, description='New user email')
