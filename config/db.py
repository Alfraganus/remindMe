import motor.motor_asyncio
from config import params

class MongoDBConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoDBConnection, cls).__new__(cls)
            cls._instance.client = motor.motor_asyncio.AsyncIOMotorClient(params.configs.get("MONGO_DB_URL"))
        return cls._instance.client

    @staticmethod
    def get_database():
        """
        Get the MongoDB database instance.
        """
        return MongoDBConnection().remindMe

    @staticmethod
    def get_collection(collection_name: str) :
        """
        Get a MongoDB collection by name.
        :param collection_name: The name of the collection.
        :return: The MongoDB collection.
        """
        return MongoDBConnection.get_database()[collection_name]
