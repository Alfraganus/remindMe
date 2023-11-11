from fastapi import FastAPI

from modules.auth.Endpoints import appAuth
from modules.todo.Routes import todoAuth
from modules.todo.jobs.test import schedular

app = FastAPI()
app.include_router(appAuth)
app.include_router(todoAuth)
# schedular.start()


