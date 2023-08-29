from pydantic import BaseModel, StrictStr, Field, condate
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


class User(BaseModel):
    login: StrictStr
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(alias="mediumPictureUrl",default=None)
    small_picture_url: Optional[StrictStr] = Field(alias="smallPictureUrl",default=None)
    status: Optional[StrictStr] = None
    rating: Rating
    online: Optional[condate] = None
    name: Optional[condate] = None
    location: Optional[StrictStr] = None
    registration: Optional[StrictStr] = None


class UserEnvelopeModel(BaseModel):
    resource: User
    metadata: Optional[StrictStr] = None
