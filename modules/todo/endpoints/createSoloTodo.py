from config.db import MongoDBConnection


async def createSoloTodo():
    my_collection = await MongoDBConnection.get_collection("todo-solor")
    result = await my_collection.insert_one({"test":"hello world"})
    return {"test": result}
