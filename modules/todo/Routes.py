from fastapi import APIRouter

from modules.todo.endpoints.createSoloTodo import createSoloTodo

todoAuth = APIRouter();

@todoAuth.post("/create-solo-todo")
async def create_solo_todo_route():
    return await createSoloTodo()
