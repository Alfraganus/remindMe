from pydantic import BaseModel


class UserRegistration(BaseModel):
    username: str
    password: str
    fullname: str
    address:  str