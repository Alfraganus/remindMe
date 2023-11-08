from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class UserRegistration(BaseModel):
    username: str
    password: str
    fullname: str
    address: str

class SoloToDo(BaseModel):
    title: str = Field("read a book", max_length=300)
    type : str = Field("General", max_length=100)
    description : str = Field("it is urgent")
    datetime : datetime

