from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    username: str
    name: str
    surname: str
    password: str
    # is_active: bool = True


