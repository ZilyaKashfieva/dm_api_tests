from datetime import datetime

from pydantic import BaseModel, StrictStr, Field, condate, StrictInt
from enum import Enum
from typing import List, Optional


class Rating(BaseModel):
    enabled: bool
    quality: int
    quantity: int


class Roles(Enum):
    GUEST = 'Guest'
    PLAYER = 'Player'
    ADMINISTRATOR = 'Administrator'
    NANNYMODERATOR = 'NannyModerator'
    REGULARMODERATOR = 'RegularModerator'
    SENIORMODERATOR = 'SeniorModerator'


class ParseMode(Enum):
    COMMON = 'Common'
    INFO = 'Info'
    POST = 'Post'
    CHAT = 'Chat'


class Info(BaseModel):
    value: Optional[StrictStr] = None
    parseMode: List[ParseMode]


class Paging(BaseModel):
    postsPerPage: Optional[StrictInt] = None
    commentsPerPage: Optional[StrictInt] = None
    topicsPerPage: Optional[StrictInt] = None
    messagesPerPage: Optional[StrictInt] = None
    entitiesPerPage: Optional[StrictInt] = None


class ColorSchema(Enum):
    MODERN = 'Modern'
    PALE = 'Pale'
    CLASSIC = 'Classic'
    CLASSICPALE = 'ClassicPale'
    NIGHT = 'Night'


class Settings(BaseModel):
    colorSchema: Optional[StrictStr] = None  # List[ColorSchema]
    nannyGreetingsMessage: Optional[StrictStr] = None
    paging: Paging


class UserDetails(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(alias="mediumPictureUrl", default=None)
    small_picture_url: Optional[StrictStr] = Field(alias="smallPictureUrl", default=None)
    status: Optional[StrictStr] = None
    rating: Rating
    online: Optional[datetime] = None
    name: Optional[condate] = None
    location: Optional[StrictStr] = None
    registration: Optional[StrictStr] = None
    icq: Optional[StrictStr] = None
    skype: Optional[StrictStr] = None
    originalPictureUrl: Optional[StrictStr] = None
    info: Optional[StrictStr] = None  # Info = None
    settings: Settings


class UserDetailsEnvelope(BaseModel):
    resource: UserDetails
    metadata: Optional[StrictStr] = None
