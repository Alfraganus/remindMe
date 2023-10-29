from models.UserResponse import UserResponse
from fastapi import FastAPI, Depends

from config.db import conn
from models.Users import users
app = FastAPI()

@app.get("/")
async def start():
    return {"text": "hello world"}

@app.get("/users",response_model=list[UserResponse])
async  def  readData():
    res = conn.execute(users.select()).fetchall()
    return res