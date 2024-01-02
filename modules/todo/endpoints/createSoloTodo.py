from config.db import MongoDBConnection
from modules.auth.schemes import SoloToDo, Notification


async def createSoloTodo(todo:SoloToDo):
    await MongoDBConnection.get_collection("todo-solo")\
        .insert_one(
        todo.dict()
    )
    return {
        "result": todo.dict(exclude={"_id"})
    }

async def createNotification(notification:Notification):
    await MongoDBConnection.get_collection("notification")\
        .insert_one(
        notification.dict()
    )
    return {
        "result": notification.dict(exclude={"_id"})
    }
