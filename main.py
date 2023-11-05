from fastapi import FastAPI
from modules.auth.services.AuthService import appAuth

app = FastAPI()
app.include_router(appAuth)

