from __future__ import annotations
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Extra, Field, StrictBool


class ResetPassword(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[str] = Field(None, description='Login')
    email: Optional[str] = Field(None, description='Email')
