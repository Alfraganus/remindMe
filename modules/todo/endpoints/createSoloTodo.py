from config.db import MongoDBConnection
from modules.auth.schemes import SoloToDo

async def createSoloTodo(todo:SoloToDo):
    await MongoDBConnection.get_collection("todo-solo")\
        .insert_one(
        todo.dict()
    )
    return {
        "result": todo.dict(exclude={"_id"})
    }
