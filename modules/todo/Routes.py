from fastapi import APIRouter
from modules.auth.schemes import SoloToDo
from modules.todo.endpoints.createSoloTodo import createSoloTodo

todoAuth = APIRouter()

@todoAuth.post("/create-solo-todo")
async def create_solo_todo_route(todo:SoloToDo):
    return await createSoloTodo(todo)
