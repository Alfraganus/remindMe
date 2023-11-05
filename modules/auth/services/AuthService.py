from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from starlette import status
from config import params
import jwt
from fastapi import APIRouter, HTTPException, Depends
from passlib.context import CryptContext
from pydantic import BaseModel
from config.db import MongoDBConnection
from modules.auth import schemes
from modules.auth.models.UserRegister import UserRegistration

appAuth = APIRouter();
authCollection = MongoDBConnection().college
users_collection = authCollection.get_collection("users")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
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



def verify_access_token(token:str, credentials_exception) :
    try:

        payload = jwt.decode(token,params.configs.get("SECRET_KEY"),algorithms=[params.configs.get("ALGORITHM")])
        id: str = payload.get("sub")
        print(payload)
        if id is None:
            raise credentials_exception
        token_Data = schemes.TokenData(id=id)
        print(token_Data)
    except JWTError as e:
        print(e)
        raise credentials_exception
    except AssertionError as e:
        print(e)
    return token_Data



async def get_current_user(token: str = Depends(oauth2_scheme)) :
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail="count not validate",headers={"WWW-Authenticate": "Bearer"})
    token = verify_access_token(token,credential_exception)
    user = await users_collection.find_one({"username": token.id})
    return user


@appAuth.get("/hello", tags=["authentication"])
async def hello_world(user_id = Depends(get_current_user)):
    return {"message": "Hello, World!"}



