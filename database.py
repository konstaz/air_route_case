import os
import pymongo



class Database:

    @classmethod
    def initialize(cls):
        client = pymongo.MongoClient(
            f'mongodb://{os.getenv("MONGO_HOST")}:{os.getenv("MONGO_PORT")}/{os.getenv("MONGO_NAME")}'
        )
        cls.database = client[f'{os.getenv("MONGO_COLLECTION")}']


    @classmethod
    def save_to_db(cls, data):
        cls.database.insert_one(data)

    @classmethod
    def load_from_db(cls, query):
        return cls.database.find(query)

    @classmethod
    def update_to_db(cls, _id, data):
        cls.database.update_one({'_id': _id}, {"$set": data})

    @classmethod
    def remove_from_db(cls, _id):
        cls.database.delete_one({'_id': _id})
