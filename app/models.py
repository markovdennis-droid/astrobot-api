from pydantic import BaseModel, Field
from typing import Literal

Sign = Literal[
    "aries", "taurus", "gemini", "cancer", "leo", "virgo",
    "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"
]

Type = Literal["daily", "weekly", "love", "career"]
Lang = Literal["ru", "en", "es"]

class HoroscopeRequest(BaseModel):
    sign: Sign = Field(...)
    type: Type = Field(...)
    lang: Lang = Field(...)
    user_type: Literal["free", "premium"] = "free"


class HoroscopeResponse(BaseModel):
    sign: Sign
    type: Type
    lang: Lang
    text: str
    is_premium_content: bool = False
from pydantic import BaseModel, Field
from typing import Literal

Sign = Literal[
    "aries", "taurus", "gemini", "cancer", "leo", "virgo",
    "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"
]

Type = Literal["daily", "weekly", "love", "career"]
Lang = Literal["ru", "en", "es"]

class HoroscopeRequest(BaseModel):
    sign: Sign = Field(...)
    type: Type = Field(...)
    lang: Lang = Field(...)
    user_type: Literal["free", "premium"] = "free"


class HoroscopeResponse(BaseModel):
    sign: Sign
    type: Type
    lang: Lang
    text: str
    is_premium_content: bool = False


