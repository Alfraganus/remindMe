from fastapi.params import Form
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from starlette import status
from config import params
import jwt
from fastapi import HTTPException, Depends
from passlib.context import CryptContext
from pydantic import BaseModel
from config.db import MongoDBConnection
from modules.auth import schemes

authCollection = MongoDBConnection().remindMe
users_collection = authCollection.get_collection("users")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

class TokenData(BaseModel):
    username: str | None = None

password_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def create_access_token(data: dict):
    return jwt.encode(data.copy(), params.configs.get("SECRET_KEY"), algorithm=params.configs.get("ALGORITHM"))

class UserLogin(BaseModel):
    username: str = Form(...)
    password: str = Form(...)


def verify_access_token(token:str, credentials_exception) :
    try:
        payload = jwt.decode(token,params.configs.get("SECRET_KEY"),algorithms=[params.configs.get("ALGORITHM")])
        id: str = payload.get("username")
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
                                         detail="count not validate",
                                         headers={"WWW-Authenticate": "Bearer"})
    token = verify_access_token(token,credential_exception)
    user = await users_collection.find_one({"username": token.id})
    return user



