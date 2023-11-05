import motor.motor_asyncio
from config import params

class MongoDBConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoDBConnection, cls).__new__(cls)
            cls._instance.client = motor.motor_asyncio.AsyncIOMotorClient(params.configs.get("MONGO_DB_URL"))
        return cls._instance.client
