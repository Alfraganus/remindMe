from fastapi import APIRouter
from modules.auth.schemes import SoloToDo, Notification
from modules.todo.endpoints.createSoloTodo import createSoloTodo, createNotification

todoAuth = APIRouter()

@todoAuth.post("/create-solo-todo")
async def create_solo_todo_route(todo:SoloToDo):
    return await createSoloTodo(todo)

@todoAuth.post("/create-notification")
async def create_notification_route(notifications:Notification):
    return await createNotification(notifications)
