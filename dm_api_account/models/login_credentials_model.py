from __future__ import annotations
from pydantic import BaseModel, Extra, Field, StrictBool
from typing import Any, Dict, List, Optional


class LoginCredentials(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[str] = None
    password: Optional[str] = None
    remember_me: Optional[StrictBool] = Field(None, alias='rememberMe')
