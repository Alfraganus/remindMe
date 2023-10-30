from fastapi import FastAPI
from modules.auth.SignUp import userModel

app = FastAPI()
app.include_router(userModel)

