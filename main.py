from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from modules.auth.Endpoints import appAuth
from modules.todo.Routes import todoAuth
from modules.todo.jobs.test import schedular

app = FastAPI()
app.include_router(appAuth)
app.include_router(todoAuth)

origins = [
    "*",
    "https://new.spector77.uz"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# schedular.start()
# test

