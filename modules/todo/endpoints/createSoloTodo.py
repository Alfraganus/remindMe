from config.db import MongoDBConnection


async def createSoloTodo():
    my_collection =  MongoDBConnection.get_collection("todo-solo")

    await my_collection.insert_one({"test": "hello world222"})
    result = await my_collection.find_one({"test": "hello world222"})  # Change the query here
    return {"test": str(result)}
