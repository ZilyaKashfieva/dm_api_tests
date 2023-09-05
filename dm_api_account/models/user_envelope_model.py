from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Extra, Field, StrictBool


class Rating(BaseModel):
    class Config:
        extra = Extra.forbid

    enabled: Optional[StrictBool] = Field(None, description='Rating participation flag')
    quality: Optional[int] = Field(None, description='Quality rating')
    quantity: Optional[int] = Field(None, description='Quantity rating')


class UserRole(Enum):
    guest = 'Guest'
    player = 'Player'
    administrator = 'Administrator'
    nanny_moderator = 'NannyModerator'
    regular_moderator = 'RegularModerator'
    senior_moderator = 'SeniorModerator'


class User(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[str] = Field(None, description='Login')
    roles: Optional[List[UserRole]] = Field(None, description='Roles')
    medium_picture_url: Optional[str] = Field(
        None, alias='mediumPictureUrl', description='Profile picture URL M-size'
    )
    small_picture_url: Optional[str] = Field(
        None, alias='smallPictureUrl', description='Profile picture URL S-size'
    )
    status: Optional[str] = Field(None, description='User defined status')
    rating: Optional[Rating] = None
    online: Optional[datetime] = Field(None, description='Last seen online moment')
    name: Optional[str] = Field(None, description='User real name')
    location: Optional[str] = Field(None, description='User real location')
    registration: Optional[datetime] = Field(
        None, description='User registration moment'
    )


class UserEnvelope(BaseModel):
    class Config:
        extra = Extra.forbid

    resource: Optional[User] = None
    metadata: Optional[Any] = Field(None, description='Additional metadata')
