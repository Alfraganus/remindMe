from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field

from modules.todo.services.ScheduleService import options


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


class Scheduler(BaseModel):
    repeat: List[str] = Field(options.get('scheduleTypes'))
    weekdays : List[int] = Field([2,3,6])

class SoloToDo(BaseModel):
    title: str = Field("read a book", max_length=300)
    type : str = Field("General", max_length=100)
    description : str = Field("it is urgent")
    notifyTime : datetime
    scheduler : Scheduler

class Notification(BaseModel):
    color: str = Field(max_length=100)
    title : str = Field(max_length=200)
    is_everyday : str = Field(max_length=50)
    oraliq_dates : List[str] = Field([])
    week_days : List[str] = Field([])
    times : List[str] = Field([])


