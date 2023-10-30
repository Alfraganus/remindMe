from modules.auth.models.UserModel import UserResponse, User, UserCreate
from fastapi import APIRouter

userModel = APIRouter()
@userModel.post('/signup', summary="Create new user")
async def create_user(user : UserCreate):

    return user
    # querying database to check if user already exist
    # user = conn.get(data.email, None)
    # if user is not None:
    #         raise HTTPException(
    #         status_code=401,
    #         detail="User with this email already exist"
    #     )
    # user = {
    #     'email': data.email,
    #     'password': get_hashed_password(data.password),
    # }
    # db[data.email] = user    # saving user to database
