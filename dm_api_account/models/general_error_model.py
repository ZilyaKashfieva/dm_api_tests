from __future__ import annotations
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Extra, Field, StrictBool


class GeneralError(BaseModel):
    class Config:
        extra = Extra.forbid

    message: Optional[str] = Field(None, description='Client message')
