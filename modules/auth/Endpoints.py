from fastapi import HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from pydantic.typing import Annotated
from modules.auth.schemes import UserRegistration
from modules.auth.services.AuthService import users_collection, UserLogin, password_context, create_access_token, \
    get_current_user

appAuth = APIRouter();

@appAuth.post("/token",tags=["authentication"])
async def token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = await users_collection.find_one({"username": form_data.username})
    if user is None or not password_context.verify(form_data.password, user.get("password_hash")):
        raise HTTPException(status_code=400, detail="Incorrect password")
    return {
        "access_token": create_access_token({"username": user["username"]}),
        "token_type": "bearer"
    }

@appAuth.post("/register", tags=["authentication"])
async def register(user_registration: UserRegistration):
    if await users_collection.find_one({"username": user_registration.username}):
        raise HTTPException(status_code=400, detail="Username already registered")
    user_data = {
        "username": user_registration.username,
        "password_hash": password_context.hash(user_registration.password),
        "fullname": user_registration.fullname,
        "address": user_registration.address,
    }
    result = await users_collection.insert_one(user_data)
    return {"user_id": str(result.inserted_id), "username": user_registration.username}


@appAuth.post("/login", tags=["authentication"])
async def logn_for_access_token(user_login: UserLogin):
    user = await users_collection.find_one({"username": user_login.username})
    if user is None or not password_context.verify(user_login.password, user.get("password_hash")):
        raise HTTPException(status_code=400, detail="Incorrect password")
    return {
        "access_token":create_access_token({"username": user["username"]}),
        "token_type": "bearer"
    }


