from config.db import MongoDBConnection
from modules.auth.schemes import SoloToDo

async def createSoloTodo(todo:SoloToDo):
    my_collection = MongoDBConnection.get_collection("todo-solo")
    await my_collection.insert_one(todo.dict())
    return {
        "result": todo.dict(exclude={"_id"})
    }
