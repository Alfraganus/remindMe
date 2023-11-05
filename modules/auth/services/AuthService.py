from config import params
import jwt
from fastapi import APIRouter, HTTPException, Depends
from passlib.context import CryptContext
from pydantic import BaseModel
from config.db import MongoDBConnection
from modules.auth.models.UserRegister import UserRegistration

appAuth = APIRouter();
authCollection = MongoDBConnection().college
users_collection = authCollection.get_collection("users")

class UserLogin(BaseModel):
    username: str
    password: str

class TokenData(BaseModel):
    username: str | None = None

password_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def create_access_token(data: dict):
    return jwt.encode(data.copy(), params.configs.get("SECRET_KEY"), algorithm=params.configs.get("ALGORITHM"))


@appAuth.post("/login", tags=["authentication"])
async def logn_for_access_token(user_login: UserLogin):
    user = await users_collection.find_one({"username": user_login.username})
    if user is None or not password_context.verify(user_login.password, user.get("password_hash")):
        raise HTTPException(status_code=400, detail="Incorrect password")
    return {
        "access_token":create_access_token({"sub": user["username"]}),
        "token_type": "bearer"
    }


@appAuth.post("/register", tags=["authentication"])
async def register(user_registration: UserRegistration):
    if await users_collection.find_one({"username": user_registration.username}):
        raise HTTPException(status_code=400, detail="Username already registered")
    user_data = {
        "username": user_registration.username,
        "password_hash": password_context.hash(user_registration.password)
    }
    result = await users_collection.insert_one(user_data)
    return {"user_id": str(result.inserted_id), "username": user_registration.username}

@appAuth.get("/hello", tags=["authentication"])
async def hello_world(secure: bool = Depends(logn_for_access_token)):
    return {"message": "Hello, World!"}